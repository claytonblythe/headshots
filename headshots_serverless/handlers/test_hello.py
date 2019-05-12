
from headshots_serverless.handlers.hello import handler

test_event = {
      "version": "0",
      "id": "01234567-0123-0123-0123-012345678901",
      "detail-type": "CodeCommit Repository State Change",
      "source": "aws.codecommit",
      "account": "123456789012",
      "time": "2017-06-12T10:23:43Z",
      "region": "us-east-1",
      "resources": [
        "arn:aws:codecommit:us-east-1:123456789012:myRepo"
      ],
      "detail": {
        "event": "referenceCreated",
        "repositoryName": "myRepo",
        "repositoryId": "12345678-1234-5678-abcd-12345678abcd",
        "referenceType": "tag",
        "referenceName": "myTag",
        "referenceFullName": "refs/tags/myTag",
        "commitId": "3e5983EXAMPLE"
      }
 }

test_context = {"blah"}
handler(test_event, test_context)