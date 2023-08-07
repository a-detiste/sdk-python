# LanPropertiesPost

## Properties
| Name | Type | Description | Notes |
| ------------ | ------------- | ------------- | ------------- |
| **ip_failover** | [**list[IPFailover]**](IPFailover.md) | IP failover configurations for lan | [optional]  |
| **ipv6_cidr_block** | **str** | [The IPv6 feature is in beta phase and not ready for production usage.] For a GET request, this value is either &#39;null&#39; or contains the LAN&#39;s /64 IPv6 CIDR block if this LAN is IPv6-enabled. For POST/PUT/PATCH requests, &#39;AUTO&#39; will result in enabling this LAN for IPv6 and automatically assign a /64 IPv6 CIDR block to this LAN. If you choose the IPv6 CIDR block on your own, then you must provide a /64 block, which is inside the IPv6 CIDR block of the virtual datacenter and unique inside all LANs from this virtual datacenter. If you enable IPv6 on a LAN with NICs, those NICs will get a /80 IPv6 CIDR block and one IPv6 address assigned to each automatically, unless you specify them explicitly on the NICs. A virtual data center is limited to a maximum of 256 IPv6-enabled LANs. | [optional]  |
| **name** | **str** | The name of the  resource. | [optional]  |
| **pcc** | **str** | The unique identifier of the private Cross-Connect the LAN is connected to, if any. | [optional]  |
| **public** | **bool** | This LAN faces the public Internet. | [optional]  |


