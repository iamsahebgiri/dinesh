import socketserver
from dns.rdtypes.ANY.TXT import TXT
import dns.message
import dns.rrset
import dns.rdataclass
import dns.rdatatype
import dns.name
import dns.rcode

from services.rand import Random
from services.echo import Echo


services = [Random, Echo]
ttl = 1


class DNSHandler(socketserver.BaseRequestHandler):
    def handle(self):
        data = self.request[0]
        socket = self.request[1]

        try:
            request = dns.message.from_wire(data)
            reply = dns.message.make_response(request)

            for question in request.question:
                qname = question.name
                name = qname.to_text()

                match name:
                    case "help.":
                        print("no?")
                        help_rrset = dns.rrset.RRset(
                            qname,
                            dns.rdataclass.IN,
                            dns.rdatatype.TXT,
                        )
                        for service in services:
                            help_txt = TXT(
                                dns.rdataclass.IN,
                                dns.rdatatype.TXT,
                                [bytes(service.help(), "utf-8")],
                            )
                            help_rrset.add(help_txt, ttl)

                        reply.answer.append(help_rrset)
                    case _:
                        err = "error: unknown query try 'dig help @127.0.0.1'"
                        error_txt = TXT(
                            dns.rdataclass.IN,
                            dns.rdatatype.TXT,
                            [bytes(err, "utf-8")],
                        )
                        err_rrset = dns.rrset.RRset(
                            qname,
                            dns.rdataclass.IN,
                            dns.rdatatype.TXT,
                        )
                        err_rrset.add(error_txt, ttl)
                        reply.answer.append(err_rrset)
                        reply.set_rcode(
                            dns.rcode.SERVFAIL
                        )  # Return 'Non-Existent Domain' error

            socket.sendto(reply.to_wire(), self.client_address)
        except Exception as e:
            print("Error:", e)


class DNSServer(socketserver.ThreadingUDPServer):
    allow_reuse_address = True
    max_packet_size = 512


if __name__ == "__main__":
    HOST, PORT = "127.0.0.1", 53
    server = DNSServer((HOST, PORT), DNSHandler)
    print(f"🚀 DNS Server started at {HOST}:{PORT}")
    server.serve_forever()
