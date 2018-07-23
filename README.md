# Movie trailers website
This webpage lists 6 movie posters, each of them is linked to a movie trailer URL.
You can browse and watch trailers by clicking on the corresponding poster.

### story
This is the first project of my Full Stack Web Developer Nanodegree program. So
for the beginning I chose 6 random movies in order to showcase my skill to generate
static webpage from python. From Udacity starter code (fresh_tomatoes.py), I added,
modified and removed some functionalities in order to improve the design and make
the webpage works the way I want. To do that, I read many online courses in different
websites such as Udacity, Udemy, W3schools, jQuery.com and getbootstrap.com .
Later on I'll make some updates for a dynamic webpage where you can watch, add,
delete and update your favourite movie trailers.
Thank you for watching.
# Usage

## Requirements
Make sure you have python installed on your computer as this application will be
run from a python file. A part from that, nothing else needs to be installed.

## Quickstart
To run this application follow the steps below:
1. Download the 3 python files : media.py, app.py and movie_trailers.py
2. Save them in the same folder on your computer
3. Open app.py in python IDLE or your favourite text editor and run it

### Command line
You can also run this command from your terminal :
`python app.py`

The webpage will automatically be opened, so you can hover over each image to
discover the movie description and you can click on it to watch the movie trailer.

## Issues
If you are running this application on Ubuntu 16.04 you may encounter the following
error being printed on your terminal:
```
###!!! [Parent][DispatchAsyncMessage] Error: PClientSource::Msg_ExecutionReady Route error: message sent to unknown actor ID

[Child 10886, MediaPlayback #1] WARNING: Decoder=9305fee0 Decode error: NS_ERROR_DOM_MEDIA_FATAL_ERR (0x806e0005) - RefPtr<mozilla::MozPromise<RefPtr<mozilla::MediaTrackDemuxer::SamplesHolder>, mozilla::MediaResult, true> > mozilla::MediaSourceTrackDemuxer::DoGetSamples(int32_t): manager is detached.: file /build/firefox-XIqkw3/firefox-59.0~b4/dom/media/MediaDecoderStateMachine.cpp, line 3453
```

First of all update your system with this command:
`sudo apt-get update`

If you have the following message at the end of the output:

`AppStream cache update completed, but some metadata was ignored due to errors.`

In this case, the problem is caused by the `appstream package version 0.9.4` that
get installed in Ubuntu 16.04 by default. You can follow this [link](https://askubuntu.com/questions/854168/how-i-can-fix-appstream-cache-update-completed-but-some-metadata-was-ignored-d) to update that package.

If you find out any other issue, please let me know. Thanks
## License
No license is needed. So you can do whatever you want with this code.
