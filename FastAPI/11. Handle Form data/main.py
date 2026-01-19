from fastapi import FastAPI, Form, File, UploadFile
from fastapi.responses import HTMLResponse
from typing import Annotated
from pydantic import BaseModel, Field
import os
import shutil
import uuid

app = FastAPI()

# @app.get("/", response_class=HTMLResponse)
# async def read_form():
#     return """
#     <html>
#         <head>
#             <title>Form Example</title>
#         </head>
#         <body>
#             <h1>Submit Your Information</h1>
#             <form action="/submit" method="post">
#                 <label for="name">Name:</label>
#                 <input type="text" id="name" name="name"><br><br>
#                 <label for="age">Age:</label>
#                 <input type="number" id="age" name="age"><br><br>
#                 <input type="submit" value="Submit">
#             </form>
#         </body>
#     </html>
#     """

# @app.post("/submit")
# async def submit_form(name: Annotated[str, Form()], age: Annotated[int, Form()]):
#     return {"name": name, "age": age}

# class FormData(BaseModel):
#     name: str = Field(min_length=3, description="Name of the user")
#     age: int = Field(gt=0, description="Age of the user")
#     model_config = {"extra": "forbid"}

# @app.post("/submit")
# async def submit_form(data: Annotated[FormData, Form()]):
#     return {"name": data.name, "age": data.age}



#File Upload Example
# @app.get("/", response_class=HTMLResponse)
# async def read_form():
#     return """
#     <html>
#         <head>
#             <title>File Upload Example</title>
#         </head>
#         <body>
#             <h1>Upload a File</h1>
#             <form action="/upload" method="post" enctype="multipart/form-data">
#                 <input type="file" name="file"><br><br>
#                 <input type="submit" value="Upload">
#             </form>
#         </body>
#     </html>
#     """

# @app.post("/upload")
# async def upload_file(file: Annotated[bytes | None, File()] = None):
#     filename = f"uploaded_{uuid.uuid4().hex}.dat"
#     save_path = os.path.join("uploads")
#     os.makedirs(save_path, exist_ok=True)
#     if file:
#         with open(os.path.join("uploads", filename), "wb") as f:
#             f.write(file)
#     return {"file_size": len(file)}

# @app.post("/upload")
# async def upload_file(file: Annotated[UploadFile | None, File()] = None):
#     filename = f"uploaded_{uuid.uuid4().hex}_{file.filename}"
#     save_path = os.path.join("uploads")
#     os.makedirs(save_path, exist_ok=True)
#     if file:
#         with open(os.path.join("uploads", filename), "wb") as f:
#             content = await file.read()
#             f.write(content)
#     return {"filename": filename, "content_type": file.content_type}



#Multiple File Upload Example
@app.get("/", response_class=HTMLResponse)
async def read_form():
    return """
    <html>
        <head>
            <title>Multiple File Upload Example</title>
        </head>
        <body>
            <h1>Upload Multiple Files</h1>
            <form action="/upload" method="post" enctype="multipart/form-data">
                <input type="file" name="files" multiple><br><br>
                <input type="submit" value="Upload">
            </form>
        </body>
    </html>
    """

@app.post("/upload")
async def upload_files(files: Annotated[list[UploadFile] | None, File()] = None):
    save_path = os.path.join("uploads")
    os.makedirs(save_path, exist_ok=True)
    file_details = []
    if files:
        for file in files:
            filename = f"uploaded_{uuid.uuid4().hex}_{file.filename}"
            with open(os.path.join("uploads", filename), "wb") as f:
                content = await file.read()
                f.write(content)
            file_details.append({"filename": filename, "content_type": file.content_type})
    return {"files": file_details}