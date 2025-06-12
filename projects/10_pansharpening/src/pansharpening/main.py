from pansharpening import data_loading


def main():
    """
    This function should have a list of all the runnable scripts that make your
    project reproducible. 
    The goal should be to fill the data/outputs folder with the results of your
    processing algorithms, including processed images, report figures and 
    tables.
    For deep learning projects, please avoid to run training scripts here.
    """
    data_loading.main()
    
    
if __name__ == "__main__":
    main()