from argparse import ArgumentParser
import pandas as pd
import os
from numpy import random

def main(input_dir, output_file):
  # read input directory for mp4 videos only
  # note: all files would be mp4 videos in the mounted input directory
  test_videos = [video for video in os.listdir(input_dir) if ".mp4" in video]

  # randomly predict probability of videos as fake
  proba = random.uniform(size=len(test_videos))

  # create output
  output_df = pd.DataFrame({"filename": test_videos, "probability": proba})

  # write ouput as csv
  output_df.to_csv(output_file, index=False)


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("-input", type=str, required=True, help="Input directory of test videos")
    parser.add_argument("-output", type=str, required=True, help="Output directory with filename e.g. /data/output/submission.csv")
    args = parser.parse_args()

    main(input_dir=args.input, output_file=args.output)