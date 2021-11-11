#!/usr/bin/env python3

from aws_cdk import core

from proxy_endpoint.proxy_endpoint_stack import ProxyEndpointStack


app = core.App()
ProxyEndpointStack(app, "proxy-endpoint")

app.synth()
