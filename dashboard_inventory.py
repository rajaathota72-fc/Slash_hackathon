import streamlit as st
st.title("SMATCH : Network of Shopify Merchants")
st.sidebar.title("Choose one")
template = """
    <div style = "background-color : black; padding : 2px;">
    <h1 style = "color:white;text-align:center;">Smart Inventory Management</h1>
    </div>
    """
st.markdown(template,unsafe_allow_html=True)
import pandas as pd
df = pd.read_csv("product.csv")
df1 = df.drop(["Wholesale price","Minimum Quantity","Maximum Quantity","Min SKU"],axis=1)
st.table(df1)
if st.sidebar.checkbox("Check stock"):
    st.success("Stock Out Products")
    list1 = list(df.Stock)
    list2 = list(df.Threshold)
    list3 = []
    for i in range(len(list1)):
        if list1[i] < list2[i]:
            list3.append("Reorder")
        else:
            list3.append("Enough stock")
    x = list3.index("Reorder")
    df1["Stock Status"] = list3
    st.dataframe(df1.iloc[x,])
    st.write("Shoe Puma is out of stock")
    st.write("Find the merchants near by for quick delivery")
    st.success("Redirecting........")
    df2 = pd.read_csv("availability.csv")
    st.table(df2)
    options = df2["Available options"]
    st.sidebar.title("select the option")
    option_selected = st.sidebar.radio("Select the Option", (1, 2, 3))
    list4 = list(df2[" cost/unit "])
    n = st.text_input("Number of units")
    if st.button("calculate"):
        if option_selected == 1:
            result = list4[0] * (int(n))
            st.success("The bill would be {}".format(result))
        elif option_selected == 2:
            result = list4[1] * (int(n))
            st.success("The bill would be {}".format(result))
        else:
            result = list4[2] * (int(n))
            st.success("The bill would be {}".format(result))
    if st.button("Check out"):
        st.success("Redirecting to payment gateway")





