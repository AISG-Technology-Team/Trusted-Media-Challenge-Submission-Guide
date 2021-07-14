# AI Singapore Trusted Media Challenge Submission Guide

Participants are to submit a **compressed Docker image in the tar.gz format** onto the [challenge platform](https://trustedmedia.aisingapore.org/competition/aisg/make-submission/). This repository serves as a step by step guide to help participants with creating a valid submission for the Trusted Media Challenge.

## Getting Started

We would be using Docker for this challenge so that participants can choose their preferred programming languages and dependencies to create the best perfoming detection models.

To build and run GPU accelerated Docker containers, please install the [NVIDIA Container Toolkit](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/install-guide.html).

## Usage of sample submission

### Clone this repository and navigate to it

```
git clone https://github.com/AISG-Technology-Team/Trusted-Media-Challenge-Submission-Example.git
```

### Change into the sample submission directory

```
cd sample_submission
```

### Build the sample Docker image

```
docker build -t sample_image .
```

_Please take note of the “.” indicates the current project directory and should be added into the docker build command to provide the build context._

### Test sample image locally

Add a few mp4 videos into local_test/test_input and replace "/path/to/cloned/repo" in the following command with the full path to the cloned repo. The test is successful if no error messages were seen and a submission.csv is created in the local_test/test_output directory.

```
docker run --rm -it \
 -v /path/to/cloned/repo/local_test/test_input:/data/input \
 -v /path/to/cloned/repo/local_test/test_output:/data/output \
 sample_image \
 -input /data/input/ -output /data/output/submission.csv
```

### Compress your sample image to .tar.gz format using [docker save](https://docs.docker.com/engine/reference/commandline/save/)

```
docker save sample_image:latest | gzip > sample_image.tar.gz
```

### Upload sample image

Submit your `sample_image.tar.gz` file onto the [challenge platform](https://trustedmedia.aisingapore.org/competition/aisg/make-submission/)

## Creating your own submission

The process of creating your own submission would be very similar to using the aforementioned sample submission.

### Create a project directory and navigate into it

```
mkdir Trusted-Media-Challenge && cd Trusted-Media-Challenge
```

### Create a main file

The main file has to accept two arguments:

- `-input` is a directory which contains all videos of the test set, e.g. /data/input/ ('/' should appear at the end of the line)
- `-output` is the name (with path) of the output file, e.g. /data/output/submission.csv

and has three main functions:

1. Read the mp4 videos from directory specified in the aforementioned `-input` argument
2. Predicts the probability that each input video is fake
3. Writes a csv output file with the name and at the path specified in the aforementioned `-output` argument. The csv file should contain two columns **filename** and **probability** where probability is the estimated probability that the video, stated in filename, is fake. An [example csv](local_test/test_output/sample_submission.csv) is provided.

You may refer to the [`main.py`](sample_submission/main.py) of the sample submission as an example of a main file.

### Create a Dockerfile

You may use the [sample Dockerfile](sample_submission/Dockerfile) provided for you. However, please install the relevant dependencies required for your detection model. Additionally, you may wish to change the ENTRYPOINT if you are using another main file or if you prefer to use a shell script:

```
ENTRYPOINT ["bash","/path/to/your/main.sh"]
```

_If you are not familiar with building a Dockerfile, please refer to the [official documentation](https://docs.docker.com/engine/reference/builder/) for more information._

### Build your Docker image using [docker build](https://docs.docker.com/engine/reference/commandline/build/)

```
docker build -t your_image .
```

_Please take note of the “.” indicates the current project directory and should be added into the docker build command to provide the build context._

### Test your image locally

#### 1. Create a test directory outside of your project directory

```
mkdir local_test && cd local_test
```

#### 2. Create input and output directory within your test directory

```
mkdir test_input test_output
```

#### 3. Add test mp4 videos into test_input directory

#### 4. Test your image using [docker run](https://docs.docker.com/engine/reference/run/)

Please replace "/path/to/test/dir" in the following command with the full path to your test directory. The test is successful if no error messages were seen and a submission.csv is created in the local_test/test_output directory.

```
docker run --rm -it --gpus ‘”device=0”’ \
 -v /path/to/test/dir/local_test/test_input:/data/input \
 -v /path/to/test/dir/local_test/test_output:/data/output \
 your_image \
 -input /data/input/ -output /data/output/submission.csv
```

_Please note that above docker run command on the [sample image](#Build-the-sample-Docker-image) would be equivalent to running the following command in the container:_

```
python /app/main.py -input /data/input/ -output /data/output/submission.csv
```

### Compress your Docker image to .tar.gz format using [docker save](https://docs.docker.com/engine/reference/commandline/save/)

```
docker save your_image:latest | gzip > your_image.tar.gz
```

### Upload your image

Submit your `your_image.tar.gz` file onto the [challenge platform](https://trustedmedia.aisingapore.org/competition/aisg/make-submission/)
