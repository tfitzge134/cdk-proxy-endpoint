import json
import pytest

from aws_cdk import core
from proxy_endpoint.proxy_endpoint_stack import ProxyEndpointStack


def get_template():
    app = core.App()
    ProxyEndpointStack(app, "proxy-endpoint")
    return json.dumps(app.synth().get_stack("proxy-endpoint").template)


def test_sqs_queue_created():
    assert("AWS::SQS::Queue" in get_template())


def test_sns_topic_created():
    assert("AWS::SNS::Topic" in get_template())
