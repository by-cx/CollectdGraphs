from plugin import MetaPluginSum


class Postfix(MetaPluginSum):
    plugin_directory = "tail-postfix"
    dst_name = "postfix"

    def gen(self):
        self.graph_meta_status("postfix-status-%s.png")
        self.graph_meta_delay("postfix-delay-%s.png")
        self.graph_meta_connections_out("postfix-connections-out-%s.png")
        self.graph_meta_connections_in("postfix-connections-in-%s.png")
        self.graph_meta_connections_rejected("postfix-rejected-%s.png")

    def graph_meta_status(self, *args):
        values = (
            ('bounced', '00e000', 'mail_counter-status-bounced.rrd', 'value'),
            ('deferred', '0000ff', 'mail_counter-status-deferred.rrd', 'value'),
            ('forwarded', 'a00000', 'mail_counter-status-forwarded.rrd', 'value'),
            ('reject', 'ff0000', 'mail_counter-status-reject.rrd', 'value'),
            ('sent', '00ff00', 'mail_counter-status-sent.rrd', 'value'),
            ('softbounce', 'f000f0', 'mail_counter-status-softbounce.rrd', 'value'),
        )
        return super(Postfix, self).graph_meta(values, *args)

    def graph_meta_delay(self, *args):
        values = (
            ('before-queue-mgr', '00e000', 'gauge-delay-before_queue_mgr.rrd', 'value'),
            ('in-queue-mgr', '0000ff', 'gauge-delay-in_queue_mgr.rrd', 'value'),
            ('trans-time', 'a00000', 'gauge-delay-trans_time.rrd', 'value'),
            ('setup-time', 'ff0000', 'gauge-delay-setup_time.rrd', 'value'),
            ('delay', '00ff00', 'gauge-delay.rrd', 'value'),
        )
        return super(Postfix, self).graph_meta(values, *args)

    def graph_meta_connections_out(self, *args):
        values = (
            ('network-unreachable', '00e000', 'mail_counter-connection-out-network-unreachable.rrd', 'value'),
            ('refused', '0000ff', 'mail_counter-connection-out-refused.rrd', 'value'),
            ('timeout', 'a00000', 'mail_counter-connection-out-timeout.rrd', 'value'),
            ('TLS-established', 'ff0000', 'mail_counter-connection-out-TLS-established.rrd', 'value'),
            ('TLS-setup', '00ff00', 'mail_counter-connection-out-TLS-setup.rrd', 'value'),
        )
        return super(Postfix, self).graph_meta(values, *args)

    def graph_meta_connections_in(self, *args):
        values = (
            ('open', '00e000', 'mail_counter-connection-in-open.rrd', 'value'),
            ('close', '0000ff', 'mail_counter-connection-in-close.rrd', 'value'),
            ('lost', 'a00000', 'mail_counter-connection-in-lost.rrd', 'value'),
            ('timeout', 'ff0000', 'mail_counter-connection-in-timeout.rrd', 'value'),
            ('TLS-established', '00ff00', 'mail_counter-connection-in-TLS-established.rrd', 'value'),
            ('TLS-setup', 'f000f0', 'mail_counter-connection-in-TLS-setup.rrd', 'value'),
        )
        return super(Postfix, self).graph_meta(values, *args)

    def graph_meta_connections_rejected(self, *args):
        values = (
            ('host-not-found', '00e000', 'mail_counter-rejected-host_not_found.rrd', 'value'),
            ('no-dns-entry', '0000ff', 'mail_counter-rejected-no_dns_entry.rrd', 'value'),
            ('rejected', 'a00000', 'mail_counter-rejected.rrd', 'value'),
            ('spam-or-forged', 'ff0000', 'mail_counter-rejected-spam_or_forged.rrd', 'value'),
        )
        return super(Postfix, self).graph_meta(values, *args)
