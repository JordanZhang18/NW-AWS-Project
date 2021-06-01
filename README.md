# NW-AWS-Project
<<<<<<< HEAD
The National Survey of Recent College Graduates, conducted from 1973 through 2015, was a cross-sectional biennial survey that provided demographic and career information about individuals holding a bachelor's or master's degree in a science, engineering, or health field from a U.S. academic institution. The survey sampled individuals living in the United States who received their degree in the prior 2 or 3 academic years and were under age 76. Results from the NSRCG help data users understand and predict trends in education, employment opportunities, and salaries of recent graduates.

The purpose of this project is to provide future college students with a visualization tool, so that they can make better informed choices when specifying a major osf study. This project extensively utilized AWS services.

---
A **Lambda function** is used to download data from CORGIS Datasets Project (corgis-edu.github.io) and write to AWS S3 bucket. Triggers can be incorporated in the future such as API or Apache Kafka. **AWS Cloud 9** was used as the IDE for development and testing.

![lambda](/static/lambda function.png)

A notebook instance is initiated in **AWS SageMaker** service. The raw dataset is read from AWS S3 and examined.  There are 516 rows and 50 columns, including survey data from 1993 to 2015 and 50 metrics regarding majors, demographics, industries and other employment information. The raw data is cleaned to reflect only the latest 2015 survey data, and 9 key metrics in form of proportions, indead of absolute number: 

* 'Demographics.Ethnicity.Minorities'
* 'Demographics.Gender.Females'
* 'Employment.Employer Type.Business/Industry'
* 'Employment.Employer Type.Educational Institution'
* 'Employment.Employer type.Government'
* 'Employment.Status.Unemployed'
* 'Education.Degrees.Bachelors'
* 'Education.Degrees.Masters'
* 'Education.Degrees.Doctorates'

Some EDA graphs are generated to examine the distribution of each metric across about 40 majors:

![box](/static/boxplot.png)

![corr](/static/corrmatrix.png)

The Correlation matrix shows limited correlation between metrics, so a predictive model is not ideal given this training set. I believe a well-tuned visualization tool to show relative distribution of demography and employment metrics across all majors will be more helpful for students than a predictive model with low confidence. The cleaned dataset is written into **AWS S3 bucket**.

A flask app is then developed to generate histograms of the selected metric, with the bin containing major of interest highlighted. The Flask app is tested and deployed using **AWS App Runner**. 

The web application can be accessed at: https://j36x2fdcwt.us-east-2.awsapprunner.com/
=======
This flask app reads employment and demographic data of graduates in various majors. And allows users to explore the distribution of multiple metrics for each major, with the major of interest highlighted.
  
Deployed using AWS app runner.
Result at: https://j36x2fdcwt.us-east-2.awsapprunner.com/
>>>>>>> 7ffa377e107e4ea5c99385494ea8dd817731d396
