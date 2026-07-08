def test_get_object(rest_client, localstack):
    key = "test_key_for_get"
    value = "test_value_for_get"

    localstack["s3_client"].put_object(
        Bucket=localstack["s3_bucket"],
        Key=key,
        Body=value.encode("utf-8"),
    )

    response = rest_client.get(f"/s3/{key}")

    assert response.status_code == 200
    assert response.text == value


def test_put_object(rest_client, localstack):
    key = "test_key_for_put"
    value = "test_value_for_put"

    response = rest_client.put(
        f"/s3/{key}",
        content=value,
        headers={"Content-Type": "text/plain"},
    )

    assert response.status_code == 204

    result = localstack["s3_client"].get_object(
        Bucket=localstack["s3_bucket"],
        Key=key,
    )

    stored_value = result["Body"].read().decode("utf-8")

    assert stored_value == value
