from cpu import CPU
from df import Df
from disk import Disk
from interface import Interface
from load import Load
from memory import Memory
from mysql_connections import MysqlConnections
from processes import Processes
from processes import ForkRate
from swap import Swap
from swap import SwapIO
from users import Users
from snmp import Snmp
from dns import DNS
from apache import Apache, ApacheScoreboard
from hddtemp import HDDTemp
from irq import IRQ
from conntrack import Conntrack

plugins_list = (
    CPU,
    Df,
    Disk,
    Interface,
    Load,
    Memory,
    MysqlConnections,
    Processes,
    ForkRate,
    Swap,
    SwapIO,
    Users,
    Snmp,
    DNS,
    Apache,
    ApacheScoreboard,
    HDDTemp,
    IRQ,
    Conntrack,
)
