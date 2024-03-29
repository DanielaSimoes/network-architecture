$TTL 604800
$ORIGIN metaltech.com.
@ IN SOA ns1.metaltech.com. adm.metaltech.com. (
                 2 ; Serial
                 604800 ; Refresh
                 86400 ; Retry
                 2419200 ; Expire
                 604800 ) ; Negative Cache TTL
         IN NS ns1.metaltech.com.
         IN A 200.1.1.1

ipv6 IN AAAA 2001:0:1::1
        IN MX 10 server1
ns1 IN A 200.1.1.1
server1 IN A 200.1.1.1
www IN CNAME server1
