# Toy Cars

A computer vision tool for gathering object location data from images and generating data visualizations. This tool was exclusively designed for an art project by Tuomas Linna.

## Assignment

Over 20000 image dataset was collected by sending 21 different toy cars down the ramp and and taking an image of each dispatch. The task was to calculate the distance traveled on every dispatch and provide a .csv-format dataset for the artist.

The distance car traveled is calculated from extracted x-coordinate and the known real-world width of the area in the image. Image metadata is also collected.

## Image processing

<figure>
    <figcaption>Example image</figcaption>
  <img
  src="docs/org.png"/>
  
  
</figure>

<figure>
    <figcaption>Blur</figcaption>
  <img
  src="docs/blur.png"/>
  
  
</figure>

<figure>
    <figcaption>Convert to grayscale</figcaption>
  <img
  src="docs/gray.png"/>
  
  
</figure>

<figure>
    <figcaption>Convert to binary image</figcaption>
  <img
  src="docs/thresh.png"/>
  
  
</figure>

<figure>
    <figcaption>Dilate to increase the size of white area in the binary image</figcaption>
  <img
  src="docs/dilate.png"/>
  
  
</figure>

<figure>
    <figcaption>Find contours in the processed image</figcaption>
  <img
  src="docs/contours.png"/>
  
  
</figure>

<figure>
    <figcaption>Find coordinates for extreme right of largest area of contours</figcaption>
  <img
  src="docs/coordinates.png"/>
  
  
</figure>

</figure>

<figure>
    <figcaption>Final</figcaption>
  <img
  src="docs/final.png"/>
  
  
</figure>

<figure>
    <figcaption>Sample CSV</figcaption>
  <img
  src="docs/csv_example.png"/>
  
  
</figure>

<figure>
    <figcaption>Debug video</figcaption>
  <img
  src="docs/014.gif"/>
  
  
</figure>
