"""
In this file I'll write html template for my webpage included css style and
javascript script. Then I'll write two python functions, the first one
'create_movie_posters_content' will dynamically create movies content that will
be injected inside the html file. The second one will create and open the html
file for the movie trailer website.
"""
import os
import re
import webbrowser

HTML_HEAD = """
<!DOCTYPE html>
<html lang="en" dir="ltr">
    <head>
        <meta charset="utf-8">
        <title>Movie Trailers</title>

        <!-- Bootstrap 4 -->
        <link rel="stylesheet" href=
        "https://stackpath.bootstrapcdn.com/bootstrap/4.1.1/css/bootstrap.min.css"
        integrity=
        "sha384-WskhaSGFgHYWDcbwN70/dfYBj47jz9qbsMId/iRN3ewGhXQFZCSftd1LZCfmhktB"
         crossorigin="anonymous">
        <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js"
        integrity=
        "sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo"
        crossorigin="anonymous"></script>
        <script src=
        "https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.3/umd/popper.min.js"
        integrity=
        "sha384-ZMP7rVo3mIykV+2+9J3UJ46jBk0WLaUAdn689aCwoqbBJiSnjAK/l8WvCWPIPm49"
        crossorigin="anonymous"></script>
        <script src=
        "https://stackpath.bootstrapcdn.com/bootstrap/4.1.1/js/bootstrap.min.js"
        integrity=
        "sha384-smHYKdLADwkXOn1EmN1qk/HfnUcbVRZyYmZ4qpPea6sjB/pTJ0euyQp0Mk8ck+5T"
        crossorigin="anonymous"></script>

         <!-- CSS -->
         <style media="screen">
             body{
                 background-color: #330000 !important;
             }
             /* Choosing a different background color for the navbar rather
             than bootstrap ones */
             .bg-movies{
                 background-color: #1a0000;
             }
             /* styling the image container*/
             .movie_thumb{
                 display: block;
                 width: 220px;
                 height: 300px;
                 margin-bottom: 30px;
             }
             /* styling the image */
             .poster{
                 position: absolute;
                 width: 100%;
                 height: 100%;
                 transition: .5s;
                 padding: 0 80px 0 80px;
             }
             /*styling the movie description that will be invisible (opacity=0)
             when the page loads. But it will appear with the "hover" event
             with a transparent black background and white font color */
             #story{
                 opacity: 0;
                 position: absolute;
                 top: 30%;
                 right: 0;
                 transition: 1s;
                 margin: 0 65px 0 50px;
                 background: rgba(0, 0, 0, 0.5);
                 color: white;
                 border-radius: 4px;
                 text-align: center;
             }
             /* The movie title will appear on the image when the page loads
             but will disappear on hover event */
             #title{
                 opacity: 1;
                 position: absolute;
                 bottom: 0;
                 left: 25%;
                 font-family: fantasy;
                 font-weight: bolder;
                 color: grey;
             }

             .navbar-brand{
                 font-family: fantasy;
             }
             /* when the mouse is hovered over the image, the image become
             transparent and is zoomed in */
             .movie_thumb:hover .poster{
                 opacity: 0.3;
                 transform: scale(1.2);
             }
             .movie_thumb:hover #story{
                 opacity: 1;
             }
             .movie_thumb:hover #title{
                 opacity: 0;
             }
             .movie_thumb:hover{
                 cursor: pointer;
             }
             /* styling the modal window */
             #trailer .modal-dialog {
                 margin-top: 200px;
                 width: 800px;
                 height: 600px;
             }
             /* positioning the close button "x" at the top right position of
             the modal window */
             .close {
                 position: absolute;
                 top: -13px;
                 right: -8px;
                 z-index: 1;
             }
             /* styling the video inside the modal window */
             .video iframe {
                 border: none;
                 height: 100%;
                 position: absolute;
                 width: 100%;
                 top: 0;
                 right: 0;
             }
             .video {
                 padding-bottom: 70%;
             }
         </style>

         <!-- javascript -->
         <script type="text/javascript">
             $(document).ready(function () {
               // Pause the video when the modal is closed
               $('.modal').on('click', '.close', function () {
                   $('#video_container').empty();
               });
               // Pause the video in modal on click outside modal
               $('#trailer').on('hidden.bs.modal', function(){
                   $('#trailer .close').trigger('click');
               });
               // Start playing the video whenever the trailer modal is opened
               $('.movie_thumb').on('click', function () {
                   var trailerYouTubeId = $(this).attr('youtube_id');
                   var url = 'https://www.youtube.com/embed/' +
                   trailerYouTubeId + '?autoplay=1&html5=1';
                   $('#video_container').append($('<iframe></iframe>', {
                       'id': 'trailer_video',
                       'type': 'text-html',
                       'src': url,
                       'frameborder': 0
                   }));
               });
             });
         </script>

    </head>
"""

HTML_BODY = """
    <!-- ##############The main page layout and title bar################## -->
    <body>
        <!-- Navbar -->
        <nav class="navbar navbar-expand-sm navbar-dark bg-movies mb-4">
            <div class="container">
                <a class="navbar-brand" href="#">Movie Trailers</a>
            </div>
        </nav>

        <!-- Movie posters -->
        <div class="container">
            <div class="row">
                {movie_posters}
            </div>
        </div>

        <!-- Trailer Video Modal -->
        <div class="modal" id="trailer">
          <div class="modal-dialog">
            <div class="modal-content">
              <button type="button" class="close" data-dismiss="modal">&times;
              </button>
              <div class="video" id="video_container">
              </div>
            </div>
          </div>
        </div>
    </body>
</html>
"""
# A single movie poster template
MOVIE_POSTER_CONTENT = """
<div class="col-sm-6 col-md-4 movie_thumb" youtube_id="{trailerYouTubeId}"
data-toggle="modal" data-target="#trailer">
    <img src="{poster_image_url}" class="poster">
    <h6 id="story">{movie_story}</h6>
    <h4 id="title">{movie_title}</h4>
</div>
"""


def create_movie_posters_content(movies):
    """
    This function extracts attributes of every single movie in the list movies:
    title, description, image URL and trailer URL. Then for each movie it fills
    the MOVIE_POSTER_CONTENT with its content.
    Parameter
    --------
    movies: a list of 6 intances of movie class
    return
    ------
    content: str
        a string of all 6 movie content
    """
    content = ''
    for movie in movies:
        # Using python regular expressions to extract the youtube ID from
        # the trailer URL knowing the youtube video ID and url format
        id_match = re.search(r'(?<=v=)[^&#]+', movie.trailer_youtube_url)
        trailer_youtube_id = id_match.group(0) if id_match else None

        # Append the tile for the movie with its content filled in
        content += MOVIE_POSTER_CONTENT.format(
            trailerYouTubeId=trailer_youtube_id,
            poster_image_url=movie.poster_image_url,
            movie_story=movie.storyline,
            movie_title=movie.title
        )

    return content


def open_movies_page(movies):
    """This function create or overwrite the html file and open it in
    the default browserself.
    Parameter
    --------
    movies: a list of 6 intances of movie class
    return
    ------
    None
        its creates the movie_trailers.html in the current working directory
        and open it in the default browser.
    """
    # Create or overwrite the output file
    output_file = open('movie_trailers.html', 'w')

    # Replace the placeholder movie_posters with the actual dynamically
    # generated content
    html_body_content = HTML_BODY.format(
        movie_posters=create_movie_posters_content(movies))

    # Output the file
    html_page = HTML_HEAD + html_body_content
    output_file.write(html_page)
    output_file.close()

    # open the output file in the browser
    url = os.path.abspath(output_file.name)
    webbrowser.open('file://' + url)
