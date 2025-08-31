#  Airbnb Analysis  

##  Project Overview  
This project analyzes **Airbnb data** using **MongoDB Atlas, Python, Streamlit, and Power BI** to uncover insights into pricing trends, seasonal availability, and location-based patterns.  
The goal is to build an **end-to-end data pipeline** – from data retrieval and cleaning to interactive dashboards – enabling **data-driven decisions** in the travel and tourism industry.  

---

## Objectives  
- Establish a **MongoDB Atlas** connection and retrieve Airbnb dataset.  
- Perform **data cleaning & preprocessing** (handle missing values, duplicates, type conversions).  
- Conduct **Exploratory Data Analysis (EDA)** using Python Notebook.  
- Build a **Streamlit web app** for interactive maps and charts.  
- Perform **geospatial analysis** to explore listing distributions.  
- Analyze **pricing variations** by location, property type, and season.  
- Explore **availability patterns** and demand fluctuations.  
- Create an **interactive Power BI dashboard** to present insights.  

---

##  Skills & Tools  
- **Programming & Analysis**: Python (Pandas, Matplotlib, Seaborn)  
- **Database**: MongoDB Atlas (NoSQL data retrieval & queries)  
- **Visualization**: Streamlit (interactive web app), Power BI (dashboard)  
- **Domain**: Travel Industry, Property Management, Tourism  

---

## Dataset  
The dataset comes from **MongoDB Atlas Airbnb data**, including details about listings, hosts, neighborhoods, prices, availability, ratings, and reviews.  

### Example JSON structure:  
```json
{
  "_id": "unique_listing_id",
  "name": "listing_title",
  "description": "listing_description",
  "host_id": "unique_host_id",
  "host_name": "host_name",
  "neighbourhood": "neighbourhood_name",
  "location": {
    "type": "Point",
    "coordinates": [longitude, latitude]
  },
  "price": "listing_price",
  "availability": {
    "start_date": "YYYY-MM-DD",
    "end_date": "YYYY-MM-DD"
  },
  "amenities": ["amenity_1", "amenity_2"],
  "rating": "average_rating",
  "reviews": [
    {
      "reviewer_id": "unique_reviewer_id",
      "reviewer_name": "reviewer_name",
      "comment": "review_comment",
      "rating": "review_rating"
    }
  ]
}
```

## Dashboard & App Preview
- Streamlit App → Interactive maps and charts.
- Power BI Dashboard → Key insights on pricing, demand, and location trends.

<img width="1159" height="651" alt="image" src="https://github.com/user-attachments/assets/c5255d14-b686-4504-9b2c-21bb250a2d9c" />

## Learning Outcomes
- **MongoDB Atlas:** Storing and retrieving Airbnb dataset efficiently.
- **Python EDA:** Data cleaning, transformation, visualization.
- **Streamlit:** Developing interactive web applications.
- **Geospatial Analysis:** Mapping Airbnb listings and trends.
- **Power BI:** Building dashboards for storytelling & decision-making.
- **End-to-End Project Execution:** From raw data to insights.

##  How to Run  

### 🔹 Python & Streamlit App  
1. Clone this repository:  
   ```bash
   git clone https://github.com/subash0812/Airbnb-analysis.git
   cd airbnb-analysis
2. Create a virtual environment and install dependencies:
   ```bash
   pip install -r requirements.txt
3. Configure your MongoDB Atlas connection in a .env file (example below):
   ```env
   MONGO_URI = "your_mongodb_connection_string"
   DB_NAME = "airbnb"
   COLLECTION_NAME = "airbnb"
4. Run the Streamlit app:
   ```bash
   streamlit run app.py

## License
- This project is licensed under the MIT License – you are free to use and adapt it.   

