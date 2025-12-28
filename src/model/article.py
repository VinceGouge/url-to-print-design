from datetime import datetime

from pydantic import BaseModel, Field, HttpUrl

class Article(BaseModel):
    title: str = Field(default=..., description="Title of the article")
    author: str = Field(default=..., description="Authors")
    hostname: str = Field(default=..., description="Base web site from which the article comes from")
    date: datetime = Field(default=..., description="Date of publication")
    text: str = Field(default=..., description="Main content")
    excerpt: str | None = Field(default=None, description="Short summary")
    image: HttpUrl | None = Field(default=None, description="Image url if any present in the article") 
    source_hostname: str | None = Field(default=None, alias="source-hostname", description="Web site name")
    source: str = Field(default=..., description="Source web site")
