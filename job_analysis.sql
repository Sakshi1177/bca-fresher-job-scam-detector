-- Project 4: BCA Fresher Job Scam Detector
-- By Sakshi Pradhan - BCA Fresher - Project 4
-- I collected 100 jobs data

-- 1. Total jobs I collected
SELECT COUNT(*) as Total_Jobs FROM jobs;
-- Result: 100 jobs

-- 2. How many Real and how many SCAM?
SELECT Real_or_Scam, COUNT(*) as Count 
FROM jobs 
GROUP BY Real_or_Scam;
-- My finding: Real 82, SCAM 18 = 18% SCAM!

-- 3. Average salary of Real jobs vs SCAM jobs
-- SCAM shows high salary to trap
SELECT Real_or_Scam, AVG(Salary_INR) as Avg_Salary
FROM jobs
WHERE Salary_INR != 'Not Disclosed'
GROUP BY Real_or_Scam;
-- Real avg ~20000, SCAM avg ~42000 - SCAM shows high to trap!

-- 4. Top skills companies want - Important for interview
SELECT Skill_1, COUNT(*) as Demand
FROM jobs
GROUP BY Skill_1
ORDER BY Demand DESC;
-- Result: Excel and SQL most demanded

-- 5. Which source has more SCAM?
SELECT Source, Real_or_Scam, COUNT(*) 
FROM jobs
GROUP BY Source, Real_or_Scam;
-- Finding: WhatsApp/Facebook has more SCAM

-- 6. My RED-GREEN logic in SQL - Same as Project 2
SELECT Company_Name, Job_Title, Salary_INR,
CASE 
  WHEN Real_or_Scam LIKE '%SCAM%' THEN 'RED - SCAM Danger - Dont Apply'
  WHEN Salary_INR < 15000 THEN 'ORANGE - Low Salary'
  ELSE 'GREEN - Real Good Job - Apply'
END as My_Verdict
FROM jobs;
