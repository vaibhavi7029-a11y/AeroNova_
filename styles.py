"""
styles.py
Premium UI Styling for AeroNova Weather Map
"""


def load_css():
    return """
    <style>

    .stApp{
        background: linear-gradient(135deg,#0f172a,#1e293b,#312e81);
        color:white;
    }

    section[data-testid="stSidebar"]{
        background:#111827;
        border-right:1px solid rgba(255,255,255,.08);
    }

    h1,h2,h3,h4,h5,p,label{
        color:white !important;
    }

    .main-title{
        font-size:42px;
        font-weight:700;
        text-align:center;
        color:white;
        margin-bottom:10px;
    }

    .sub-title{
        text-align:center;
        color:#cbd5e1;
        font-size:18px;
        margin-bottom:30px;
    }

    .glass-card{
        background:rgba(255,255,255,0.08);
        backdrop-filter:blur(15px);
        border-radius:18px;
        padding:22px;
        border:1px solid rgba(255,255,255,0.15);
        box-shadow:0 8px 30px rgba(0,0,0,.35);
        margin-bottom:20px;
    }

    .metric-title{
        color:#94a3b8;
        font-size:14px;
    }

    .metric-value{
        color:white;
        font-size:30px;
        font-weight:bold;
    }

    .weather-title{
        text-align:center;
        font-size:28px;
        font-weight:bold;
        color:white;
    }

    .footer{
        text-align:center;
        color:#94a3b8;
        font-size:14px;
        margin-top:30px;
    }

    div.stButton > button{
        width:100%;
        border-radius:12px;
        height:50px;
        border:none;
        color:white;
        background:linear-gradient(90deg,#2563eb,#7c3aed);
        font-weight:bold;
        transition:.3s;
    }

    div.stButton > button:hover{
        transform:scale(1.03);
        background:linear-gradient(90deg,#1d4ed8,#6d28d9);
    }

    input{
        border-radius:10px !important;
    }

    </style>
    """
