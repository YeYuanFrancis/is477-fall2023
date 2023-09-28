# Reproduction of: Retiring Adult - New Datasets for Fair Machine Learning (IS477)
## Overview
This repository serves as reproducing specific results from the paper "Retiring Adult: New Datasets for Fair Machine Learning". This is part of the IS477 course on Data Management, Curation, and Reproducibility. To make sure the study results are correct, the project will use a normal logistic regression model on two sets of data: the original UCI Adult dataset and a rebuilt version of that dataset that is shown in the paper. The project wants to see how fair and accurate machine learning models are at making predictions about people from different groups. For machine learning and data processing, we will use Python. For version control and code management, we will use Git and GitHub. Results include the model's performance measures, datasets that have been cleaned and preprocessed, well-documented code, and a detailed README that can be used again and again.


## Data Availability

### Origin of Datasets

1. **UCI Adult Dataset**: This dataset was obtained from the UCI Machine Learning Repository.Becker,Barry and Kohavi,Ronny. (1996). Adult. UCI Machine Learning Repository. https://doi.org/10.24432/C5XW20.
  
2. **Reconstructed Dataset**: This dataset was was derived from IPUMS CPS data, the dataset is part of the Folktables repository [https://github.com/socialfoundations/folktables/blob/main/adult_reconstruction.csv].

### Copyright and Licensing

1. **UCI Adult Dataset**: The dataset is generally available for public use for educational and research purposes. This dataset is licensed under a Creative Commons Attribution 4.0 International (CC BY 4.0) license.
2. **Reconstructed Dataset**: The data itself is governed by the terms of use provided by the Census Bureau. The data are intended for replication purposes only. Individuals analyzing the data for other purposes must submit a separate data extract request directly via IPUMS CPS. Individuals are not to redistribute the data without permission.

### Justification for Inclusion/Exclusion of Datasets

Due to copyright considerations, I have decided not to include the Reconstructed dataset directly in this repository, because this dataset are only intended for replication purposes. For others to obtain copies of the data, you will need to ask for redistribution requests. 


## Software License

This project is licensed under the MIT License. By choosing it, I hope to give back to the open-source community and let people use the software for free. 

This license is Permissive. The MIT License is easy to understand and lets anyone use, change, and share the program. For its Compatibility, A lot of other agreements work with the MIT License, which makes it easier to work with other open-source projects. It does not have Strong Copyleft If you make changes to something using the MIT License, you don't have to share it under the same license. This is different from licenses that have strict copyleft rules. This gives us more options for how to use and improve it in the future. It is widely used: The MIT License is a well-known license in the open-source world, and it gives people some peace of mind that the rules will be clear and followed.


## Data License

The data and models in this repository are licensed under the Creative Commons Attribution 4.0 International License (CC BY 4.0). By using the CC BY 4.0 License, I hope to make it easier for people to share data that can be used upon, while still making sure that the original makers get credit. 

With its attribution, the license says that people who use your data and models must give you credit, link back to the license, and say if they made any changes. This makes sure that people who contributed are properly thanked. CC BY 4.0 is very liberal, like the MIT License for our software. It lets both academic and business users use, change, and share the licensed data. The license can be used anywhere in the world, even if your country doesn't have copyright rules that protect it.



References:
Ding, F., Hardt, M., Miller, J., & Schmidt, L. (2022). Retiring Adult: New Datasets for Fair Machine Learning. arXiv. https://doi.org/10.48550/arXiv.2108.04884.
Becker,Barry and Kohavi,Ronny. (1996). Adult. UCI Machine Learning Repository. https://doi.org/10.24432/C5XW20.