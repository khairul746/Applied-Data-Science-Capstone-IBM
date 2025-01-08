# Applied Data Science Capstone IBM

## Project Overview
This capstone project focuses on predicting the success of the Falcon 9 first stage landing. 
SpaceX offers Falcon 9 rocket launches at $62 million per flight, significantly 
lower than other providers, who charge up to $165 million. The cost savings primarily 
come from SpaceX's ability to reuse the rocket’s first stage. Therefore, predicting 
the likelihood of a successful landing can help estimate the overall launch cost, 
providing valuable insights for competitors looking to bid against SpaceX for 
similar services.

This capstone project serves as the final assignment in the IBM Data Science 
certification. The project follows a structured approach, with each phase completed 
in separate notebooks. It begins by collecting data via APIs in the first notebook, 
followed by preprocessing in the second. Afterward, exploratory data analysis (EDA) 
is conducted to uncover hidden patterns, with visualizations created using tools 
like Matplotlib, Seaborn, and DashPlotly. In the final stage, a machine learning 
model is developed to predict the outcome of the rocket launches. Among the trained 
models, the Decision Tree achieved the highest performance with an F1 score of 0.88, 
making it the most suitable model for this task.

## Data
The data for this project was collected using SpaceX APIs, providing detailed 
information on Falcon 9 rocket launches, including mission outcomes and 
technical specifications. This real-world dataset forms the foundation for 
analyzing and predicting the success of Falcon 9 first-stage landings.

## Methodology
- **Data Collection** : Obtained through APIs.
- **Data Preprocessing** : Cleaned and prepared the raw data to ensure consistency and usability.
- **Exploratory Data Analysis** : Utilized visualizations and statistical techniques with tools like Matplotlib, Seaborn, and DashPlotly to uncover patterns and insights.
- **Model Development** : Built machine learning models to predict the success of rocket landings, testing algorithms such as Decision Trees, Support Vector Machine, k-Nearest Neighbor,and Logistic Regression.
- **Evaluation** : Compared models using metrics like F1 score, with the Decision Tree emerging as the top performer (F1 score = 0.88). 

## Results
The project successfully developed a predictive model to estimate the likelihood of Falcon 9 first-stage landing success.  
The Decision Tree model demonstrated the best performance, indicating its suitability for similar prediction tasks.

## Future Scope
1. **Model Optimization**: Experiment with ensemble techniques or deep learning models to enhance performance further.

2. **Interactive Dashboards**: Develop user-friendly dashboards for stakeholders to analyze predictions and visualize results dynamically.

3. **Cost Analysis**: Extend the analysis to estimate the financial impact of successful and failed landings on overall mission profitability.

---
