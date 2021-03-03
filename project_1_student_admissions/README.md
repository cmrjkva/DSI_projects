
# Problem Statement:

   Let's say: I work for a the University of Colorado - Boulder.  We have a lot of applications and we cannot accept all that would like to come to CU Boulder or we would be overcrowded. We are going to use the SAT to selectivly decide a lower threshold of students we will not consider unless there have reasonable exceptionalities. We also want to split up the students based on their prospective majors and have  some standards for entry into the departments of study with in the college for those students that will right away begin work in their prospective major. 
  
   I want to see how people perform in the math and reading/writing section of the SAT in regards to their respective majors of interest as well. Perhaps they may be of more importance to specific colleges, such as math to the engineering department. It is a matter of curiousity for me to see if their strengths on test scores are a reflection of their major choices. 

  Thus with the available data, we are tasked with finding the scores spread of last years test takers with consideration for their declared college majors and for setting up a rubric of expectations for the college departments. We will have to bunch up the majors into selected colleges and we will need to select the minimum test scores required for entry into individual colleges based of the entry standards of the university. 
    
    
# DATA DICTIONARY:

|Feature|Type|Dataset|Description|
|---|---|---|---|
|a_slist|list|SAT|List of indices that select the art and science majors|  
| arlist|list|ACT/SAT|This is the acceptance rate converted from object to float | 
| art_science_school|dataset|SAT|dataset of majors in the art and science majors| 
| blist|list|SAT|list of indices that select business majors| 
| business_school|dataset|SAT|majors in the business department| 
| collegelist|list|SAT|list of departments by indices to match original dataset of college majors| 
| elist|elist|SAT|Majors in the engineering department| 
| engineering_school|dataset|SAT|Majors in the engineering department| 
| law_school|dataset|SAT|Majors in the law department| 
| majorsinschool|dataset|SAT|Majors in the CU Boulder system| 
| manualmean |func |NA |This calculates mean| 
| manualsd |func |NA|This calculates standard deviation| 
| meanforplot|dict |SAT|This gives mean SAT scores of incoming students by prospective major| 
| media_communication_school|dataset|SAT|dataset of majors in media department| 
| p2float |func |ACT/SAT|Percent to Float| 
| percentlist|list|ACT/SAT|list of percents (acceptance rate)| 
| sat2019_college_major|dataset|SAT|Primary dataset with SAT scores by prospective majors| 
| sat25list|list|SAT|list of 25th percentiles for accepted college students| 
| sat75list|list|SAT|list of 75th percentiles for accepted college students|
| sat_act_college|datasett|ACT/SAT|Primary dataset with all the colleges listed with detailes about acceptance rates, SAT and ACT scores, and more... | 
| satfatlist|list|SAT|75th and 25th percentiles for all colleges| 
| schoollist|list|SAT|list of names of the college departments| 
| test_takers|list|SAT|numbers of test takers by each prospective major| 
| whatevernum|int|ACT/SAT|Same whatever numbers for testing calculations| 

    
    

    
    
# Breif Summary of Analysis:


  We are making a few general assumptions. We are assuming that:
  gratuations rates and SAT scores have a correlation, 
  that must stick to our acceptance rate and that we will not be doing a more holistic method of determining enrollment until later in the enrollment process, 
  and that students with low SAT scores will not be initially accepted to the deparetment of choice for their prospective majors. 

  I used the dataset that included all the universites to get the important information on the University of Colorado as well as their admissions website. We needed their acceptance rate, number of applicants, and the SAT scores ranges for accepted students. From there I used my other dataset, to see how students who have declared their major stack up with their overall SAT scores. 

  I realized that I needed to make a new datafram where the major choices were grouped into the departments of the college they belong too, se we could do visuals and take calculations. Our goal here is to help determine department guidlines for admissions. I was able to formulate the mean, the 25th and 75 percentiles, and create a histogram & scatterplot that provided some helpful information.  



# Conclusion/Recommendations:
    
  I determined a lower SAT standard for Engineering at 1045, Arts & Science at 1059 and Business 1032. Students who score less than these scores should not be granted enrollment unless there is are exceptianal reasons why the student could succeed otherwise, such as taking remedial classes before entering, or displaying abilities in other ways. The histogram also indicates that there is a more normal distribution of math scores than reading/writing sections. 

 
 
 
# Resources


   I found Boulder's actual first year admissions for each college standards. This will be a good fact checker. Also displays all the colleges offered and what majors they entail.
   
https://www.colorado.edu/admissions/first-year/selection

   This is the degree programs offered and the majors. 
https://www.colorado.edu/academics/programs?field_degree_prog_college_school_tid=268#undefined
    
https://www.colorado.edu/academics/programs?field_degree_prog_college_school_tid=268#arts--sciences-college-of
    
    
    
https://www.cu.edu/cu-facts-and-figures
    
   Photo Credits to Bentley University for Art & Science : STEAM - Science and the Arts: If You Can’t Beat Them, Join Them (victoryprd.com)
        Scales Of Justice Free Stock Photo - Public Domain Pictures
    All public domain free photos

https://www.tutorialspoint.com/python3/string_strip.htm
https://stackoverflow.com/questions/25669588/convert-percent-string-to-float-in-pandas-read-csv
    
    