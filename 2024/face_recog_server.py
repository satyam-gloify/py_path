"""Having Installation issue 
I tried executing this:
pip3 install distribute
problem solved?
Also resolved by
pip install setuptools
"""

import face_recognition
import asyncio 
import websockets
import json, io

picture_of_me= face_recognition.load_image_file("assets/mypic.png")
my_face_encoding = face_recognition.face_encodings(picture_of_me)[0]

async def websocket_handler(websocket, path):
    try:
        async for message in websocket:
            response = recognize_face(message)
        await websocket.send(json.dumps(response))
    except Exception as e:
        print(f"WebSocket Error: {str(e)}")

def recognize_face(message):
    try:
        print(1)
        unknown_picture = face_recognition.load_image_file(io.BytesTO(message));
        unknown_face_encodings = face_recognition.face_encodings(unknown_picture)
        print(2)
        if len(unknown_face_encodings > 0):
            unknown_face_encoding = unknown_face_encodings[0]
        else:
            return {"status": True,"Message": "No Face Detected", "data": 0}
        results = face_recognition.Compare_faces([my_face_encoding], unknown_face_encoding)
        print(4)
        print (results)
        if results[0] ==True:
            return {"status": True, "Bessage": "Recognition successtul", "data": 2}
        else:
            return {"status": True, "Message": "Recognition unsuccessful", "data": 1}
    except Exception as e:
        return {"status": False, "message":str(e)}

if __name__ =='__main__':
    loop=asyncio.get_event_loop()
    loop.run_until_complete(
        websockets.serve(websocket_handler,"0.0.0.0",8765)
    )
    loop.run_forever()
# if __name__ == '__main__':
#     loop = asyncio.new_event_loop()
#     asyncio.set_event_loop(loop)
#     try:
#         asyncio.run( websockets.serve(websocket_handler,"0.0.0.0",8765))
#     except KeyboardInterrupt:
#         pass