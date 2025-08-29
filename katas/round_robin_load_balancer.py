class IP:
    """
    Represents an IPv4 address.
    """

    def __init__(self, address: str):
        """
        Initializes an IP address.

        Args:
            address: The IP address as a string.

        Raises:
            ValueError: If the address is invalid.
        """
        if not self._is_valid_ip(address):
            raise ValueError(f"Invalid IP address: {address}")
        self.address = address

    def _is_valid_ip(self, address: str) -> bool:
        """
        Validates an IPv4 address.
        """
        parts = address.split(".")
        if len(parts) != 4:
            return False
        for p in parts:
            if not p.isdigit():
                return False
            # Disallow leading zeros (except single zero)
            if len(p) > 1 and p[0] == '0':
                return False
            n = int(p)
            if n < 0 or n > 255:
                return False
        return True

    def __str__(self):
        return self.address

    def __eq__(self, other):
        return isinstance(other, IP) and self.address == other.address

    def __hash__(self):
        return hash(self.address)


class RoundRobinLoadBalancer:
    """
    Implements a round-robin load balancer.
    """

    def __init__(self):
        self._servers: list[IP] = []
        self._index: int = 0

    def add_server(self, server: IP):
        if server in self._servers:
            return
        self._servers.append(server)

    def remove_server(self, server: IP):
        if server not in self._servers:
            return
        removed_index = self._servers.index(server)
        self._servers.remove(server)
        # Adjust index: if we removed a server before or at current index, shift back one
        if self._servers:
            if removed_index < self._index or self._index >= len(self._servers):
                self._index = self._index % len(self._servers)
        else:
            self._index = 0

    def route_request(self) -> IP | None:
        if not self._servers:
            return None
        server = self._servers[self._index]
        self._index = (self._index + 1) % len(self._servers)
        return server



if __name__ == '__main__':
    lb = RoundRobinLoadBalancer()

    lb.add_server(IP("192.168.0.1"))
    lb.add_server(IP("192.168.0.2"))
    lb.add_server(IP("192.168.0.3"))

    print("Routing to:", lb.route_request())  # Should route to 192.168.0.1 server
    print("Routing to:", lb.route_request())  # Should route to 192.168.0.2 server
    print("Routing to:", lb.route_request())  # Should route to 192.168.0.3 server
    print("Routing to:", lb.route_request())  # Should route to 192.168.0.1 server again

    lb.remove_server(IP("192.168.0.2")) # Remove second server

    print("Routing to:", lb.route_request()) # Should route to 192.168.0.3 server
    print("Routing to:", lb.route_request()) # Should route to 192.168.0.1 server again
