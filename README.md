# Claim-Classifier-Tiktok

**EN:** Development of an end-to-end classification pipeline to analyze TikTok content. This project spans from exploratory data analysis (EDA) of engagement metrics to building and evaluating a Logistic Regression model to predict user and claim verification status.  
**ES:** Desarrollo de un pipeline de clasificación de extremo a extremo para analizar contenido de TikTok. Este proyecto abarca desde el análisis exploratorio de datos (EDA) de métricas de interacción hasta la construcción y evaluación de un modelo de Regresión Logística para predecir el estado de verificación de usuarios y reclamos.

---

## 🔍 Project Overview / Descripción del Proyecto

* **Client / Cliente:** TikTok Data Team
* **Goal / Objetivo:** Build a discriminative classifier for claim and verification detection. / Construir un clasificador discriminativo para la detección de reclamos y verificación.
* **Framework / Marco:** PACE (Plan, Analyze, Construct, Execute)
* **Tools / Herramientas:** Python (Pandas, NumPy, Scikit-Learn, Matplotlib), Jupyter, Markdown.

---

## 📊 Key Results & Model Metrics / Resultados Clave y Métricas del Modelo

### 1. Confusion Matrix Breakdown / Desglose de la Matriz de Confusión
* **True Negatives (TN):** 1,589 | **False Positives (FP):** 1,960 *(Type I Error)*
* **False Negatives (FN):** 506 *(Type II Error)* | **True Positives (TP):** 3,099

### 2. Analytical Insights / Hallazgos Analíticos
* **EN:** The Logistic Regression model achieved high sensitivity (**Recall**), capturing $86\%$ of verified accounts ($3,099$ out of $3,605$). However, it displays a strong bias, misclassifying $55.2\%$ of unverified accounts as verified (**False Positives**). Feature analysis through log-odds coefficients reveals that account verification is driven by deep engagement patterns (`text_length` and `video_comment_count`) rather than raw viral metrics like views or downloads.
* **ES:** El modelo de Regresión Logística logró una alta sensibilidad (**Recall**), capturando el $86\%$ de las cuentas verificadas ($3,099$ de $3,605$). Sin embargo, muestra un sesgo marcado, clasificando erróneamente el $55.2\%$ de las cuentas no verificadas como verificadas (**Falsos Positivos**). El análisis de importancia de variables mediante coeficientes de *log-odds* revela que la verificación está impulsada por patrones de interacción profunda (`text_length` y `video_comment_count`) en lugar de métricas virales brutas como vistas o descargas.

---

## 📂 Repository Structure / Estructura del Repositorio

* `tiktok-verification-logistic-regression.ipynb` → Final production notebook containing feature engineering (One-Hot Encoding), model alignment, and evaluation. / Notebook final de producción que contiene ingeniería de variables, alineación de matrices y evaluación.
* `/docs/` → Executive summaries, strategic assessments, and stakeholder briefs. / Resúmenes ejecutivos e informes para partes interesadas.
* `/notebooks/` → Historical notebooks for initial inspection, EDA, and exploratory modeling. / Notebooks históricos de inspección inicial y EDA.

---

## 🚀 Next Steps / Próximos Pasos
* **EN:** Transition from linear decision boundaries to non-linear tree-based machine learning models (**Random Forest** and **XGBoost**) to reduce the False Positive rate and optimize classification precision.
* **ES:** Transicionar de fronteras de decisión lineales a modelos de aprendizaje automático no lineales basados en árboles (**Random Forest** y **XGBoost**) para reducir la tasa de Falsos Positivos y optimizar la precisión de la clasificación.
