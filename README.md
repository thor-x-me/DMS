# DMS
This project is on DMS (Driver Monitoring System). We will track drivers movements and send him alert about if he is taking care about the road or not while driving.

## Training
- Training a model is easy when you have your data formated properly.
- Classification traing data follows following structure here:
- The folder 'data' is stored in project file DMS
  <p>data <br>
    |<br>
      -train<br>
          | <br>
            --Active <br>
            --Drowsy <br>
      -val <br>
          | <br>
            --Active <br>
            --Drowsy <br> </p>
  



<h2> Video Streaming </h2>
 - Using Flask For Live Streaming the Video .
<br>
 <h3>Streaming.py</h3>

- This python script creates a Flask web application that serves a video stream from the webcam.
<br>
- It initializes the Flask app and creates a video capture object using opencv to access the default webcam.
<br>
- The generate_frames() function continuously captures frames from the webcam and yields them as a response.
<br>
- If the script is run directly (__name__ == "__main__"), it starts the Flask application.

<h3> index.html </h3>

- It includes a title and img tag to display the video stream. <br>

- The src attribute of the img tag is set to the /video route using Flask's url_for() function, which fetches the video stream

<h3>File Structure </h3>

Stream <br>
| <br>
-Video_Streaming <br>
 |<br>
-Streaming.py <br>
-Templates/index.html