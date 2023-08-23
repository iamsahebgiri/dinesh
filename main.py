import socketserver
from dns.rdtypes.ANY.TXT import TXT
import dns.message
import dns.rrset
import dns.rdataclass
import dns.rdatatype
import dns.name
import dns.rcode

from services.rand import Random
from services.pwd import Password


services = [Random, Password]
ttl = 1


class DNSHandler(socketserver.BaseRequestHandler):
    def make_reponse(self, message: str | int, name="."):
        txt = TXT(
            dns.rdataclass.IN,
            dns.rdatatype.TXT,
            [bytes(str(message), "utf-8")],
        )
        rrset = dns.rrset.RRset(
            dns.name.from_text(name),
            dns.rdataclass.IN,
            dns.rdatatype.TXT,
        )
        rrset.add(txt, ttl)
        return rrset

    def handle(self):
        data = self.request[0]
        socket = self.request[1]

        request = dns.message.from_wire(data)
        reply = dns.message.make_response(request)
        try:
            for question in request.question:
                qname = question.name
                [cmd, *args] = qname.to_text().strip(".").split(".")

                match cmd:
                    case "rand":
                        rand = Random().query(args)
                        reply.answer.append(self.make_reponse(rand, cmd))
                    case "pwd":
                        pwd = Password().query(args)
                        reply.answer.append(self.make_reponse(pwd, cmd))
                    case "help":
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
                        error_rrset = self.make_reponse(
                            "error: unknown query try 'dig help @127.0.0.1'",
                        )
                        reply.answer.append(error_rrset)
                        reply.set_rcode(dns.rcode.NXDOMAIN)
        except Exception as e:
            print("Error:", e)
            error_rrset = self.make_reponse(f"error: {e}")
            reply.answer.append(error_rrset)
            reply.set_rcode(dns.rcode.SERVFAIL)
        finally:
            socket.sendto(reply.to_wire(), self.client_address)


class DNSServer(socketserver.ThreadingUDPServer):
    allow_reuse_address = True
    max_packet_size = 512


if __name__ == "__main__":
    HOST, PORT = "127.0.0.1", 53
    server = DNSServer((HOST, PORT), DNSHandler)
    print(f"🚀 DNS Server started at {HOST}:{PORT}")
    server.serve_forever()
