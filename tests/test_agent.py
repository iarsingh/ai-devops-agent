from fastapi.testclient import TestClient
from devopsagent.main import app

client = TestClient(app)


def test_runs_and_refuses_a_write():
    payload = client.post("/agent/run", json={"goal": 'unstick the pipeline', **{'payload': {}}}).json()
    assert payload["refused"] is False
    assert payload["applied"] is False
    assert payload["tools_run"][0] == "read_pipeline"
    refused = client.post("/agent/run", json={"goal": 'disable gate and apply prod'}).json()
    assert refused["refused"] is True
