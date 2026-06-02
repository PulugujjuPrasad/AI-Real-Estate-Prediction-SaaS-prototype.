# AI Real Estate Prediction SaaS Prototype — 100 Questions & Answers

This file documents 100 key questions and answers for the AI Real Estate Prediction SaaS Prototype. It is intended for product engineering, stakeholder review, onboarding, and documentation purposes.

1. Q: What is the AI Real Estate Prediction SaaS Prototype?
   A: It is a Streamlit-based Python prototype that allows users to upload real estate datasets, explore properties with filterable cards, and run automated price predictions using a local machine learning model.

2. Q: Which file contains the main application logic?
   A: `app.py` contains the Streamlit UI, data loading, filtering, model training, and prediction logic.

3. Q: What file holds Python dependencies?
   A: `requirements.txt` lists the required Python libraries for the project.

4. Q: What dataset is included for demo use?
   A: `data/sample_properties.csv` is the built-in dataset used for demonstration and testing.

5. Q: Which web framework is used?
   A: Streamlit is used as the web app framework for the prototype.

6. Q: What model is used for predictions?
   A: A `RandomForestRegressor` from scikit-learn is used to build the local prediction model.

7. Q: How does the app detect the price column?
   A: It searches columns for keywords like `price`, `sale`, `value`, or `amount` and selects the first match.

8. Q: What happens if no price target column is found?
   A: The app will still show the dataset and filters, but model training and prediction are disabled.

9. Q: What file stores Streamlit configuration?
   A: `.streamlit/config.toml` stores the app server settings and theme customizations.

10. Q: What is the purpose of `docs/PRD.md`?
    A: It documents the product requirements, vision, target users, and feature scope.

11. Q: What is the purpose of `docs/BRD.md`?
    A: It documents business objectives, success metrics, requirements, and stakeholder alignment.

12. Q: Why is the README updated?
    A: To provide clear setup instructions, project overview, file organization, and alignment with PRD/BRD.

13. Q: What are the required dataset formats?
    A: `.csv`, `.xlsx`, and `.xls` are supported.

14. Q: Can users filter by city?
    A: Yes, if the dataset contains a `City` column, the app provides a city filter.

15. Q: Can users filter by neighborhood?
    A: Yes, if the dataset contains a `Neighborhood` or `Neighbourhood` column.

16. Q: How are numeric features scaled?
    A: Numeric features are standardized using `StandardScaler`.

17. Q: How are categorical features encoded?
    A: Categorical features are encoded using `OneHotEncoder`.

18. Q: Which evaluation metrics does the app show?
    A: It displays Mean Absolute Error (MAE) and R² score.

19. Q: What is the default port used by Streamlit?
    A: Port `8501` is the default for local execution.

20. Q: How do you run the app in Codespaces?
    A: Use `python -m streamlit run app.py --server.headless true --server.port 8501`.

21. Q: Does the app support file upload through the browser?
    A: Yes, the sidebar has a file uploader for CSV and Excel files.

22. Q: What happens when the user uploads data?
    A: The app loads the dataset, detects available columns, and enables filters and prediction if possible.

23. Q: How does the app handle missing target rows?
    A: It drops rows missing target values before training the model.

24. Q: How does the app handle missing feature values?
    A: It fills missing values with zero in the model training dataset.

25. Q: How many columns are shown after filtering?
    A: The app displays the filtered results table using all available columns in the dataset.

26. Q: Are there sample screenshots in the README?
    A: The README includes placeholder screenshot guidance; actual assets can be added under `/assets/`.

27. Q: What is the significance of `.gitignore`?
    A: It prevents environment files, temporary files, and build artifacts from being committed.

28. Q: What is the `props` of the model pipeline?
    A: The pipeline includes preprocessing and a RandomForest regressor.

29. Q: Can the app load a dataset from a local path?
    A: Yes, users can enter a local path in the sidebar when running locally.

30. Q: What is the default sample dataset used when no file is uploaded?
    A: `data/sample_properties.csv` is loaded automatically if present.

31. Q: Does the app support both `.xlsx` and `.xls` Excel files?
    A: Yes, it supports both `.xlsx` and `.xls` using `openpyxl`.

32. Q: Why is `openpyxl` required?
    A: It is needed to read Excel files with pandas.

33. Q: Can the app be extended to support more charts?
    A: Yes, Plotly is already installed and can be used to add visual analytics.

34. Q: What is the default Streamlit theme?
    A: The app uses a custom theme defined in `.streamlit/config.toml`.

35. Q: Can the app run without sample data?
    A: Yes, if a user uploads their own dataset, it can run without the sample file.

36. Q: What is the main purpose of the BDR and PRD docs?
    A: They provide alignment for product scope and business strategy.

37. Q: What is the expected user action flow?
    A: Upload or load dataset, explore filters, view results, and use prediction if price data is detected.

38. Q: Is the app suitable for stakeholder demos?
    A: Yes, it is designed as a prototype demo for product and business stakeholders.

39. Q: How is the header rendered in the app?
    A: A banner image and title are rendered at the top of the Streamlit page.

40. Q: What does `st.set_page_config` configure?
    A: It sets the page title, page icon, and layout style.

41. Q: What is `SAMPLE_DATA_PATH` used for?
    A: It points to the built-in sample dataset file.

42. Q: How does the app pick an image for property cards?
    A: The `get_property_image` function selects an Unsplash URL based on property type.

43. Q: How many property cards are shown at most?
    A: It shows up to 12 filtered property cards.

44. Q: Does the app support a sidebar help text option?
    A: Yes, there is a checkbox to show explanatory help text.

45. Q: How does the app warn users when no data is loaded?
    A: It displays a Streamlit warning message.

46. Q: What happens when the `Enter local path` option is used?
    A: The user can type a path to a local dataset file to load.

47. Q: What are common valid target column names?
    A: `SalePrice`, `Price`, `Value`, `Sale Amount`.

48. Q: Is the app currently production-ready?
    A: It is a prototype; production readiness requires more validation and deployment hardening.

49. Q: What should be added for production deployment?
    A: Secure configuration, database integration, and more robust model evaluation.

50. Q: Can the README be improved with actual screenshots?
    A: Yes, adding image assets under `/assets/` and linking them in the README will improve documentation.

51. Q: What is the expected user benefit of the prototype?
    A: Rapid validation of real estate data insights and model-driven price estimation.

52. Q: Why is the `data/` folder included?
    A: To store sample and local datasets used by the app.

53. Q: Can the app display remote images for property types?
    A: Yes, it loads default images from Unsplash URLs.

54. Q: How is model training triggered?
    A: It runs automatically when a valid target price column is detected.

55. Q: What is the impact of one-hot encoding on model inputs?
    A: It converts categorical variables into numeric indicator features.

56. Q: Can the app currently handle multi-tenant datasets?
    A: It is built for a single dataset upload and local analysis only.

57. Q: Does the project include a `.venv` folder?
    A: Yes, but it should be excluded from source control by `.gitignore`.

58. Q: What is the purpose of `requirements.txt` in this repo?
    A: To ensure the correct Python packages are installed for reproducibility.

59. Q: How can the app show feature distributions?
    A: Plotly or Streamlit charts can be added to visualize numeric and categorical distributions.

60. Q: Which project files are central to the app?
    A: `app.py`, `requirements.txt`, `.streamlit/config.toml`, and `data/sample_properties.csv`.

61. Q: What should users do if the dataset has unexpected column names?
    A: Rename key columns or modify the app’s column mapping logic.

62. Q: Is the app’s model suitable for all property datasets?
    A: It is a general prototype model; dataset-specific tuning may be needed.

63. Q: Can developers add support for maps later?
    A: Yes, adding coordinates and a map component is a clear extension.

64. Q: What does the app do with date fields?
    A: It does not currently process date fields; they are included as raw features if numeric.

65. Q: Can the app handle boolean columns?
    A: Yes, boolean columns are treated as categorical features.

66. Q: How does the app deal with unseen categories during prediction?
    A: `OneHotEncoder(handle_unknown="ignore")` ignores unseen categories safely.

67. Q: Which code section builds the model?
    A: The `build_model` function constructs the preprocessing pipeline and fits the model.

68. Q: What is the default test split ratio?
    A: The app uses `train_test_split` with `test_size=0.2`.

69. Q: Is the model trained on the full dataset?
    A: It is trained on 80% of the available rows and evaluated on 20%.

70. Q: Can users manually select prediction features?
    A: Not in the current version; the model uses all numeric and categorical columns.

71. Q: Why are some columns dropped from modeling?
    A: The target column is dropped and only feature columns remain.

72. Q: What is the fallback value if the dataset is empty?
    A: An empty DataFrame is returned and the app shows a warning.

73. Q: Can the app show the dataset row count?
    A: Yes, it displays the number of rows and columns loaded.

74. Q: What is the UI layout style?
    A: The app uses a wide layout with sidebar controls and a main content area.

75. Q: How is the page title set?
    A: With `st.set_page_config(page_title=...)`.

76. Q: What is the default page icon?
    A: A house emoji `🏡`.

77. Q: Can the README be used as a pitch document?
    A: Yes, it includes overview, setup, project scope, and next steps.

78. Q: What kind of users should see the BRD?
    A: Stakeholders, product owners, and business reviewers.

79. Q: What kind of users should see the PRD?
    A: Engineering and product teams planning feature work.

80. Q: Why include a Q&A file?
    A: It helps reviewers quickly understand project capabilities, assumptions, and extension opportunities.

81. Q: What is the main prototype use case?
    A: Visualizing and predicting property prices from uploaded datasets.

82. Q: Why is `server.enableCORS = false` in the Streamlit config?
    A: It is set for development environment behavior, but it conflicts with XSRF protection.

83. Q: What warning does Streamlit display on startup?
    A: It warns `server.enableCORS=false` is not compatible with `server.enableXsrfProtection=true`.

84. Q: How should that warning be addressed?
    A: Update `.streamlit/config.toml` to remove or align conflicting security settings.

85. Q: Does the app currently include asset screenshots?
    A: No, it includes screenshot guidance but no actual image assets.

86. Q: What folder would store screenshot assets?
    A: Create an `/assets/` folder for screenshot files if needed.

87. Q: What should be included in the app instructions?
    A: Data loading steps, filter guidance, model prediction flow, and troubleshooting notes.

88. Q: Does the prototype support custom image sources?
    A: Not currently, but it can be extended with user-provided property image URLs.

89. Q: Can the app detect property type automatically?
    A: It uses column values from `Property Type` or `PropertyType` when available.

90. Q: What is the expected behavior if the dataset contains duplicate columns?
    A: Pandas will load duplicates, but this may cause ambiguous column selection and should be avoided.

91. Q: How can a developer improve model explainability?
    A: Add feature importance, SHAP values, or partial dependence charts.

92. Q: What does `create_prediction_form` do?
    A: It renders input widgets for model features and predicts the target value when submitted.

93. Q: How does the app generate default slider ranges?
    A: It uses the dataset min/max values for numeric features.

94. Q: Can the app currently handle multi-sheet Excel files?
    A: No, it only loads the default first sheet via pandas.

95. Q: What is the app's main data validation gap?
    A: It lacks explicit schema validation and assumes reasonably structured input.

96. Q: How can users contribute to the prototype?
    A: They can provide improved datasets, screenshots, UI enhancements, and model refinements.

97. Q: What are the next development priorities?
    A: Add screenshot assets, improve dataset mapping, enrich prediction inputs, and add summary analytics.

98. Q: Is the project ready for a product demo?
    A: Yes, as a functional prototype with data upload, property exploration, and prediction capability.

99. Q: What should be updated in the README after adding screenshots?
    A: Replace placeholders with real image embeds or links to screenshot files.

100. Q: How can the project be pushed to GitHub after changes?
     A: Add and commit the files, then use `git push origin main`.
