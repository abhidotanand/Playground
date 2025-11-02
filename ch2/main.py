from fastapi import FastAPI, Form, File, UploadFile
from fastapi.responses import HTMLResponse
from typing import Annotated
from pydantic import BaseModel, Field
import os
import uuid
import shutil
app = FastAPI()

#Simple form for testing
# @app.get("/", response_class=HTMLResponse)
# async def read_form():
#     return """
#     <html>
#         <body>
#             <h2>Login Form</h2>
#             <form action="/login/" method="post">
#                 <label for="username">Username:</label><br>
#                 <input type="text" id="username" name="username"><br>
#                 <label for="password">Password:</label><br>
#                 <input type="password" id="password" name="password"><br><br>
#                 <input type="submit" value="Submit">
#             </form>
#         </body>
#     </html>
#     """

# @app.post("/login/")
# async def login(username: Annotated[str, Form()], password: Annotated[str, Form()]):
#     return {"username": username, "password": len(password) * "*"}  # Masking password length for security

# class LoginForm(BaseModel):
#     model_config = {"extra": "forbid"}  # Forbid extra fields not defined in the model
#     username: str = Field(min_length=3)
#     password: str = Field(min_length=6)

# @app.post("/login/")
# async def login(form_data: Annotated[LoginForm, Form()]):
#     return {"username": form_data.username, "password": len(form_data.password) * "*"}  # Masking password length for security

#====================FILE UPLOAD========================
# @app.get("/", response_class=HTMLResponse)
# async def main():
#     return """
#     <html>
#         <body>
#             <h2>Single File Upload (bytes)</h2>
#             <form action="/uploadfile/" enctype="multipart/form-data" method="post">
#                 <input name="file" type="file">
#                 <input type="submit" value="Upload">
#             </form>
#         </body>
#     </html>
#     """

# @app.post("/uploadfile/")
# async def upload_file(file: Annotated[UploadFile, File()]):
#     file_location = f"uploads/{str(uuid.uuid4())}.bin"
#     os.makedirs("uploads", exist_ok=True)
#     with open(file_location, "wb") as buffer:
#         shutil.copyfileobj(file.file, buffer)
#     return {"info": f"file saved at {file_location}"}

# @app.get("/", response_class=HTMLResponse)
# async def main():
#     return """
#     <html>
#         <body>
#             <h2>Single File Upload (bytes)</h2>
#             <form action="/uploadfiles/" enctype="multipart/form-data" method="post">
#                 <input name="files" type="file" multiple>
#                 <input type="submit" value="Upload">
#             </form>
#         </body>
#     </html>
#     """

# @app.post("/uploadfiles/")
# async def upload_files(files: Annotated[list[UploadFile], File()]):
#     os.makedirs("uploads", exist_ok=True)
#     file_locations = []
#     for file in files:
#         file_location = f"uploads/{str(uuid.uuid4())}_{file.filename}"
#         with open(file_location, "wb") as buffer:
#             shutil.copyfileobj(file.file, buffer)
#         file_locations.append(file_location)
#     return {"info": f"files saved at {file_locations}"}