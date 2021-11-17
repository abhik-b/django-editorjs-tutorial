from django.db import models
from django_editorjs import EditorJsField
# Create your models here.

class Post(models.Model):
    title=models.CharField(max_length=60)
    body=EditorJsField(
        editorjs_config={
            "tools":{
                "Link":{
                    "config":{
                        "endpoint":
                            '/linkfetching/'
                        }
                },
                "Image":{
                    "config":{
                        "endpoints":{
                            "byFile":'/uploadi/',
                            "byUrl":'/uploadi/'
                        },
                       
                    }
                },
                "Attaches":{
                    "config":{
                        "endpoint":'/uploadf/'
                    }
                }
            }
        }
    )

    