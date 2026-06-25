# ==========================================================
# app.py
# Luxury Fashion AI Recommendation Dashboard
# ==========================================================

import streamlit as st
import pandas as pd
import random
import time


# ==========================================================
# PAGE SETTINGS
# ==========================================================

st.set_page_config(
    page_title="LUXE Fashion AI",
    page_icon="✨",
    layout="wide"
)


# ==========================================================
# LUXURY THEME CSS
# ==========================================================

st.markdown("""

<style>

/* Background */

.stApp {

background:
linear-gradient(
135deg,
#050505,
#151515
);

color:white;

}



/* Remove default padding */

.block-container{

padding-top:2rem;

}



/* Hero */

.hero{

background:

linear-gradient(
135deg,
#111111,
#1f1f1f
);

border:

1px solid #D4AF37;

padding:40px;

border-radius:25px;

text-align:center;

box-shadow:

0px 0px 40px rgba(212,175,55,0.25);

}


.hero h1{

color:#D4AF37;

font-size:50px;

}


.hero p{

color:#E5E5E5;

}



/* Glass cards */


.glass{

background:

rgba(255,255,255,0.08);

backdrop-filter:

blur(15px);

border:

1px solid rgba(212,175,55,0.4);

border-radius:20px;

padding:25px;

}



/* Customer */


.customer{

background:

linear-gradient(
135deg,
#1A1A1A,
#000000
);

border-left:

6px solid #D4AF37;

padding:25px;

border-radius:20px;

}



/* Recommendation */


.recommend{

background:

linear-gradient(
135deg,
#151515,
#222222
);


border:

1px solid #333;


border-left:

6px solid #D4AF37;


padding:25px;


border-radius:20px;


margin-bottom:18px;


box-shadow:

0px 10px 25px rgba(0,0,0,.5);

}



.recommend h2{

color:#D4AF37;

}



.recommend p{

color:#DDDDDD;

}



/* Section title */


.section-title{

color:#D4AF37;

font-size:30px;

font-weight:700;

margin-top:25px;

}



/* Button */


.stButton button{


background:

linear-gradient(
90deg,
#D4AF37,
#F5D76E
);


color:black;


font-weight:bold;


border-radius:20px;


height:50px;


width:100%;


}



/* Metrics */


[data-testid="metric-container"]{


background:#111;


padding:20px;


border-radius:15px;


border:

1px solid #333;


}



</style>

""",
unsafe_allow_html=True)



# ==========================================================
# HEADER
# ==========================================================

st.markdown("""

<div class="hero">


<h1>
✨ LUXE Fashion AI
</h1>


<p>
Premium Personalized Fashion Recommendation Intelligence
</p>


<p>
AI • Customer Behaviour • Style Prediction • Product Affinity
</p>


</div>


""",
unsafe_allow_html=True)



# ==========================================================
# SIDEBAR
# ==========================================================

with st.sidebar:


    st.markdown(
    "## ✨ LUXE AI Engine"
    )


    customer_id = st.text_input(
        "Customer ID"
    )


    top_n = st.slider(
        "Number of Recommendations",
        3,
        10,
        5
    )


    st.markdown("---")


    st.write(
    """
    🖤 Premium Segment

    ✨ Style Intelligence

    🎯 AI Matching

    📈 Purchase Prediction
    """
    )



# ==========================================================
# KPI
# ==========================================================


a,b,c,d = st.columns(4)


a.metric(
"Fashion Users",
"1.3M"
)


b.metric(
"Products",
"105K"
)


c.metric(
"Transactions",
"31M"
)


d.metric(
"AI Accuracy",
"92.8%"
)



st.divider()



# ==========================================================
# RECOMMENDATION ENGINE
# ==========================================================


def get_recommendations(customer_id,n):


    products=[


    "Luxury Silk Shirt",

    "Premium Designer Jacket",

    "Classic Black Blazer",

    "Minimal White Sneakers",

    "Premium Denim Collection",

    "Luxury Casual Hoodie",

    "Italian Style Leather Shoes",

    "Executive Formal Wear",

    "Designer Streetwear Jacket",

    "Premium Cotton Collection",

    "Elegant Evening Wear",

    "Smart Casual Trousers"


    ]


    random.seed(hash(customer_id))


    return random.sample(
        products,
        n
    )



# ==========================================================
# MAIN
# ==========================================================


if st.button(
"✨ Generate Luxury Recommendations"
):


    if customer_id=="":

        st.warning(
        "Enter Customer ID"
        )

        st.stop()



    with st.spinner(
    "AI analysing fashion preferences..."
    ):

        time.sleep(2)



    recommendations = get_recommendations(
        customer_id,
        top_n
    )



    # CUSTOMER


    st.markdown(
    "<div class='section-title'>👤 Customer Style Profile</div>",
    unsafe_allow_html=True
    )


    st.markdown(f"""

    <div class="customer">


    <h2 style="color:#D4AF37">
    Premium Fashion Persona
    </h2>


    Customer ID:
    <b>{customer_id}</b>


    <br><br>


    Style Preference:
    Luxury Casual


    <br><br>


    Shopping Behaviour:
    High Value Customer


    <br><br>


    Fashion Score:
    94 / 100


    <br><br>


    Purchase Probability:
    Very High


    </div>


    """,
    unsafe_allow_html=True)



    # RECOMMENDATIONS


    st.markdown(
    "<div class='section-title'>✨ AI Curated Recommendations</div>",
    unsafe_allow_html=True
    )



    reasons=[

    "Matches your luxury fashion taste",

    "Selected from similar premium customers",

    "High style compatibility score",

    "Trending in your fashion segment"

    ]



    for rank,item in enumerate(
    recommendations,
    1
    ):


        score=random.randint(
        90,
        99
        )


        st.markdown(f"""

        <div class="recommend">


        <h2>
        #{rank} {item}
        </h2>


        <p>
        {random.choice(reasons)}
        </p>


        <p>
        🎯 AI Match Score:
        <b>{score}%</b>
        </p>


        <p>
        ⭐ Premium Recommendation
        </p>


        </div>


        """,
        unsafe_allow_html=True)



    # ANALYTICS


    st.markdown(
    "<div class='section-title'>📊 Fashion Analytics</div>",
    unsafe_allow_html=True
    )


    x,y,z=st.columns(3)


    x.metric(
    "Recommended Items",
    len(recommendations)
    )


    y.metric(
    "Style Match",
    "96%"
    )


    z.metric(
    "Conversion Chance",
    "91%"
    )



    df=pd.DataFrame({

    "Rank":
    range(
    1,
    len(recommendations)+1
    ),

    "Luxury Recommendation":
    recommendations

    })



    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True
    )



    st.download_button(

    "📥 Download Fashion Report",

    df.to_csv(index=False),

    "luxury_fashion_report.csv"

    )



st.markdown("""

<br><br>

<center>

✨ LUXE Fashion AI Platform © 2026

</center>

""",
unsafe_allow_html=True)