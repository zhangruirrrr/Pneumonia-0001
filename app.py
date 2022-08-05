{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 32,
   "metadata": {},
   "outputs": [],
   "source": [
    "from flask import Flask, render_template, request\n",
    "from werkzeug.utils import secure_filename\n",
    "from skimage import io\n",
    "from keras.models import load_model\n",
    "import cv2\n",
    "from PIL import Image #use PIL\n",
    "import numpy as np"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "metadata": {},
   "outputs": [],
   "source": [
    "app=Flask(__name__)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " * Serving Flask app \"__main__\" (lazy loading)\n",
      " * Environment: production\n",
      "\u001b[31m   WARNING: This is a development server. Do not use it in a production deployment.\u001b[0m\n",
      "\u001b[2m   Use a production WSGI server instead.\u001b[0m\n",
      " * Debug mode: off\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      " * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)\n",
      "127.0.0.1 - - [04/Aug/2022 22:43:04] \"GET / HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [04/Aug/2022 22:43:04] \"GET /favicon.ico HTTP/1.1\" 404 -\n",
      "[2022-08-04 22:43:12,631] ERROR in app: Exception on / [POST]\n",
      "Traceback (most recent call last):\n",
      "  File \"d:\\anaconda\\lib\\site-packages\\flask\\app.py\", line 2447, in wsgi_app\n",
      "    response = self.full_dispatch_request()\n",
      "  File \"d:\\anaconda\\lib\\site-packages\\flask\\app.py\", line 1952, in full_dispatch_request\n",
      "    rv = self.handle_user_exception(e)\n",
      "  File \"d:\\anaconda\\lib\\site-packages\\flask\\app.py\", line 1821, in handle_user_exception\n",
      "    reraise(exc_type, exc_value, tb)\n",
      "  File \"d:\\anaconda\\lib\\site-packages\\flask\\_compat.py\", line 39, in reraise\n",
      "    raise value\n",
      "  File \"d:\\anaconda\\lib\\site-packages\\flask\\app.py\", line 1950, in full_dispatch_request\n",
      "    rv = self.dispatch_request()\n",
      "  File \"d:\\anaconda\\lib\\site-packages\\flask\\app.py\", line 1936, in dispatch_request\n",
      "    return self.view_functions[rule.endpoint](**req.view_args)\n",
      "  File \"C:\\Users\\hp\\AppData\\Local\\Temp\\ipykernel_1844\\3564131563.py\", line 6, in upload_t\n",
      "    file.save(app.config(\"./static/\"+filename)) #Heroku no need static\n",
      "TypeError: 'Config' object is not callable\n",
      "127.0.0.1 - - [04/Aug/2022 22:43:12] \"POST / HTTP/1.1\" 500 -\n",
      "[2022-08-04 22:43:49,863] ERROR in app: Exception on / [POST]\n",
      "Traceback (most recent call last):\n",
      "  File \"d:\\anaconda\\lib\\site-packages\\flask\\app.py\", line 2447, in wsgi_app\n",
      "    response = self.full_dispatch_request()\n",
      "  File \"d:\\anaconda\\lib\\site-packages\\flask\\app.py\", line 1952, in full_dispatch_request\n",
      "    rv = self.handle_user_exception(e)\n",
      "  File \"d:\\anaconda\\lib\\site-packages\\flask\\app.py\", line 1821, in handle_user_exception\n",
      "    reraise(exc_type, exc_value, tb)\n",
      "  File \"d:\\anaconda\\lib\\site-packages\\flask\\_compat.py\", line 39, in reraise\n",
      "    raise value\n",
      "  File \"d:\\anaconda\\lib\\site-packages\\flask\\app.py\", line 1950, in full_dispatch_request\n",
      "    rv = self.dispatch_request()\n",
      "  File \"d:\\anaconda\\lib\\site-packages\\flask\\app.py\", line 1936, in dispatch_request\n",
      "    return self.view_functions[rule.endpoint](**req.view_args)\n",
      "  File \"C:\\Users\\hp\\AppData\\Local\\Temp\\ipykernel_1844\\3564131563.py\", line 6, in upload_t\n",
      "    file.save(app.config(\"./static/\"+filename)) #Heroku no need static\n",
      "TypeError: 'Config' object is not callable\n",
      "127.0.0.1 - - [04/Aug/2022 22:43:49] \"POST / HTTP/1.1\" 500 -\n",
      "127.0.0.1 - - [04/Aug/2022 22:44:05] \"GET /favicon.ico HTTP/1.1\" 404 -\n",
      "127.0.0.1 - - [04/Aug/2022 22:44:06] \"GET /favicon.ico HTTP/1.1\" 404 -\n",
      "127.0.0.1 - - [04/Aug/2022 22:44:06] \"GET / HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [04/Aug/2022 22:44:07] \"GET /favicon.ico HTTP/1.1\" 404 -\n",
      "[2022-08-04 22:44:27,749] ERROR in app: Exception on / [POST]\n",
      "Traceback (most recent call last):\n",
      "  File \"d:\\anaconda\\lib\\site-packages\\flask\\app.py\", line 2447, in wsgi_app\n",
      "    response = self.full_dispatch_request()\n",
      "  File \"d:\\anaconda\\lib\\site-packages\\flask\\app.py\", line 1952, in full_dispatch_request\n",
      "    rv = self.handle_user_exception(e)\n",
      "  File \"d:\\anaconda\\lib\\site-packages\\flask\\app.py\", line 1821, in handle_user_exception\n",
      "    reraise(exc_type, exc_value, tb)\n",
      "  File \"d:\\anaconda\\lib\\site-packages\\flask\\_compat.py\", line 39, in reraise\n",
      "    raise value\n",
      "  File \"d:\\anaconda\\lib\\site-packages\\flask\\app.py\", line 1950, in full_dispatch_request\n",
      "    rv = self.dispatch_request()\n",
      "  File \"d:\\anaconda\\lib\\site-packages\\flask\\app.py\", line 1936, in dispatch_request\n",
      "    return self.view_functions[rule.endpoint](**req.view_args)\n",
      "  File \"C:\\Users\\hp\\AppData\\Local\\Temp\\ipykernel_1844\\3564131563.py\", line 6, in upload_t\n",
      "    file.save(app.config(\"./static/\"+filename)) #Heroku no need static\n",
      "TypeError: 'Config' object is not callable\n",
      "127.0.0.1 - - [04/Aug/2022 22:44:27] \"POST / HTTP/1.1\" 500 -\n"
     ]
    }
   ],
   "source": [
    "@app.route(\"/\", methods=[\"GET\", \"POST\"])\n",
    "def upload_t():\n",
    "    if request.method=='POST':\n",
    "        file=request.files['file']\n",
    "        filename=secure_filename(file.filename)\n",
    "        file.save(app.config(\"./static/\"+filename)) #Heroku no need static\n",
    "        file=open(app.config(\"./static/\"+filename,\"r\")) #Heroku no need static\n",
    "        model=load_model(\"Pneumonia\")\n",
    "        image=cv2.imread(\"./static/\"+filename)\n",
    "        gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)\n",
    "        img=cv2.merge([gray,gray,gray])\n",
    "        img.resize((150,159,3))\n",
    "        img=np.asarray(img,dtype=\"float32\") #need to transfer to np to reshape\n",
    "        img=img.reshape(1,img.shape[0],img.shape[1],img.shape[2]) #rgb to reshape to 1,100,100,3\n",
    "        pred=model.predict(img)\n",
    "        return(render_template(\"index.html\",result=str(pred)))\n",
    "    else:\n",
    "        return(render_template(\"index.html\",result=\"WAITING\"))\n",
    "\n",
    "if __name__==\"__main__\":\n",
    "    app.run()"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3.9.12 ('base')",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.12"
  },
  "orig_nbformat": 4,
  "vscode": {
   "interpreter": {
    "hash": "5179d32cf6ec497baf3f8a3ef987cc77c5d2dc691fdde20a56316522f61a7323"
   }
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
