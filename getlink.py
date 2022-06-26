import requests
import urllib3

headers = {
    'Host': 'dynamodb.eu-west-1.amazonaws.com',
    # 'Content-Length': '678',
    'Sec-Ch-Ua': '" Not A;Brand";v="99", "Chromium";v="96"',
    'Sec-Ch-Ua-Mobile': '?0',
    'Authorization': 'AWS4-HMAC-SHA256 Credential=ASIAQS72XPUWMVOWVA6B/20220619/eu-west-1/dynamodb/aws4_request, SignedHeaders=host;x-amz-content-sha256;x-amz-date;x-amz-security-token;x-amz-target;x-amz-user-agent, Signature=6c285c4eef2997183e1833d7185c4eb76e6100c7fb856f0c03c4ec0ef556fa73',
    'Content-Type': 'application/x-amz-json-1.0',
    'X-Amz-Content-Sha256': 'dff80708d4e230cd36ab275c85d9497138696822e84c7b8e675e0e9e9f4864cd',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36',
    'X-Amz-Security-Token': 'IQoJb3JpZ2luX2VjEP3//////////wEaCWV1LXdlc3QtMSJHMEUCIQDp+kmkO3eAC7qmFJ9YQBXLGFqucEXI9HEpPGB/4A7tTgIgJz/Q59qbmvrRbh6WxAIuBQCM/a0Ckvo6CqHXCGmyFcsqkQYIFhACGgwwNDA3OTExNDU3NzIiDEbElZMNl8EJNk89oyruBaxANJAYeyx7mvpCFvvRvTq8J858VFnHx0QwL6XpDLuyKd+d+McoXogbs0lwgrVHzy2t+dqG091Hd3hwci8oTfL8rM9C5vHl2oHWofHYN1L9LRUpFtir36vHxbnlQKan7NwWFIySEwksV+1gRH1tYB9JkznWPlXB9x9gOshf9Rf9tBXNJLyEYohlmhO9lc+eWIgT0XAfYfjcCrFeFnWLVpvm4YtZaKu/3DiczxCWVeUT4xNlQy8Y/5IwA07d4REKtUw2CkvWtP0VWaMzsId+QMqgCAOndMV4mgEUK3EKpqdKfGM0W8jWV3YMdO7d1+ynCF+vWbIwZrpRDQZvoxZdaFxqcc48MozS9xJkoorMO+ZioQ1uexidKs74DnjZr0IFSbsvWvgHjksZVCS9ZIxcImD8hl8gVHx++PkphWAEPR3GgB60YIzGJ5QylQBn/voiS0QaDMa79WsqglMVE9dWnmgolD2jphbxLaGDayM7NiiBMKC0Tc/1JQE0Lam5qZ8ZCP2tcu1/oOnBZlwi7+AfuPCdKdJrdOSB2FcmY136CyeKwFhz1TXwcUgHXcFdh95y9e4LOjtmqXkblhgXFvp/Rb/cgeeG3Jgv4HlEMBTCJAVs4WY5NVDRhM+oeUECTplty8Gd7PnMxrXOCWQePsBLV/p0n745q99WI9SQZpIwcPDhsOk/I1bEO2xZd5l2y6lfDnwh7d3UNHvNpTL4CvFSmqZMXgGCI0NQltEEUiuICP5qfVeC61ktuz9hxdZ/T8phpFfaVZCohIiIoopIqTXT0atl2bYRUVtWjv6kv+0Vx8dD9+tv+6yo3lA5UwPdkGFmHFL4Z6SlPvn+TqYSwpxiLkib4jNdfcphMcZpPH61vFzb2cF1Q8YVWZ+7xypSEM3b3kAs9jZORDkJIc2ed/A+HKZjN3JCRiTQQgjt2UhLJ2VA1RQn0xSpFkPGRmXeqWSy5MWTgJsFKMnSOiodv6T5xPqV00hQ/CfSuV8e6SEqJDCSsryVBjqHAnFfNGt/V8TeolU+0NLkvB9AB+RJ9+Y1SaQgI6Y6LaM/2foU/04LMQZxJuSsiLa3uEZ4SNJJ8EiLPtAcnA4VSsURyGwMYUz/cFuUOHPcVClIMq83Xa6qZR2Tmnw1jprZeN0jQj7RkV8+cyrTjptYb2xNc7ukM9j7XcSnLrlNIPT0ilcZGSTyzc1X7OVsMNDLNlMHy+UQOJG+TLsHsA0l/Gm/YPGo9eil6PZ38wmzOIiMSLx4ZgJXVkARWwT2a41PEN/qFpr7uDlvjchi8J2zYRfVebJy0bUkfD4XD/K1Q+s7N8uo+zsMj0UcBexp4DDPQAzNk5M5uyxGrzA7u6s/ElJtPO7QQa61',
    'X-Amz-Target': 'DynamoDB_20120810.Query',
    'X-Amz-Date': '20220619T132453Z',
    'X-Amz-User-Agent': 'aws-amplify/0.4.x js aws-amplify/0.4.x js promise',
    'Sec-Ch-Ua-Platform': '"Linux"',
    'Accept': '*/*',
    'Origin': 'https://privatedelights.ch',
    'Sec-Fetch-Site': 'cross-site',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': 'https://privatedelights.ch/',
    # 'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.9',
    'Connection': 'close',
}

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

data = '{"TableName":"geo","KeyConditions":{"hashKey":{"ComparisonOperator":"EQ","AttributeValueList":[{"N":"-916"}]},"geohash":{"ComparisonOperator":"BETWEEN","AttributeValueList":[{"N":"-9162573441885274111"},{"N":"-9160321642071588865"}]}},"IndexName":"geohash-index","ConsistentRead":false,"ReturnConsumedCapacity":"NONE","FilterExpression":"  ( attribute_not_exists(owner_hide) or owner_hide = :false ) ","ExpressionAttributeValues":{":false":{"BOOL":false}},"ScanIndexForward":false,"ProjectionExpression":"un, owner_hide, hide, m,be,bs,pe,se,mse,ps, geoJson, rangeKey, rkey, c, images, available, #time, #country","ExpressionAttributeNames":{"#time":"time","#country":"country"}}'

response = requests.post('https://dynamodb.eu-west-1.amazonaws.com/', headers=headers, data=data, verify=False)

print(response.text)