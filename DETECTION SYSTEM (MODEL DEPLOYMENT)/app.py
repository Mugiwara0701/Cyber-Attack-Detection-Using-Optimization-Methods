import numpy as np
import pickle
import streamlit as st


# loading the saved model 
loaded_model = pickle.load(open("D:/CYBER ATTACK DETECTION PROJECT/DETECTION SYSTEM (MODEL DEPLOYMENT)/trained_model.pkl",'rb'))

# creating a function for detection 

def attack_detection(input_data):
        # changing data to numpy array 
    input_data_array = np.asarray(input_data)
    
    # reshape the array as we are predicting for one instance
    input_data_reshaped =  input_data_array.reshape(1,-1)
    
    result = loaded_model.predict(input_data_reshaped)
    print("The prediction is : ",result)
    
    if (result[0] == 0):
      return "NO ATTACK FOUND"
    else:
      return "ATTACK FOUND"

  

def main():
    # giving a title 
    st.markdown("<h1 style='text-align: center; color: blue;'>Cyber Attack Detection</h1>", unsafe_allow_html=True)
    
    # getting the input data from input user
    duration = st.text_input("Input the duration  : ")
    orig_bytes = st.text_input("Input the source bytes : ")
    resp_bytesc = st.text_input("Input the response bytes : ")
    missed_bytes = st.text_input("Input the missed bytes : ")
    orig_pkts = st.text_input("Input the orignal packets: ")
    orig_ip_bytes = st.text_input("Input the orignal ip bytes : ")
    resp_pkts = st.text_input("Input the response packets : ")
    resp_ip_bytes= st.text_input("Input the respnose ip bytes: ")
    misses_bytes = st.text_input("Input the missing bytes : ")
    proto_encoded = st.text_input("Input the Protocal : ")
    conn_state_encoded = st.text_input("Input the Connection state : ")


    # code for prediction 
    detect = '' # null string 
    
    # creating a button for detection 
    
    if st.button('Input Test Result'):
        detect = attack_detection([duration, orig_bytes, resp_bytesc,missed_bytes,orig_pkts,orig_ip_bytes,resp_pkts,resp_ip_bytes,misses_bytes,proto_encoded, conn_state_encoded])
        
    st.success(detect)
    
    st.markdown("***")
    st.markdown(""" Protocol and Connection State Label Encoded info

     Proto icmp = 0
     Proto udp = 1
     Proto tcp = 2
     Connection State S0 = 6 (Connection attempt seen, no reply yet)
     Connection State OTH = 0 (No SYN seen, just midstream traffic)
     Connection State SF = 10 (Normal establishment and termination)
     Connection State REJ = 1 (Connection attempt rejected)
     Connection State S3 = 9 
     Connection State RSTR = 4 (Connection established, responder aborted)
     Connection State RSTO = 2 (Connection established, originator aborted)
     Connection State RSTOS0 = 3 (Originator sent a SYN followed by a RST, no response from responder)
     Connection State S1 = 7 (Connection established, not terminated)
     Connection State S2 = 8 
     Connection State RSTRH = 5 (Responder sent a SYN ACK followed by a RST, no response from originator)
     Connection State SH = 11
     Connection State SHR = 12 (Same as SYN_SENT)
    """)
    
    
    st.text("\n\n")
    st.markdown("<h3 style='text-align: center; color: blue;'>Model accuracy is 73.498% </h3>", unsafe_allow_html=True)
    
    
    st.write(" \n\n\n\n\n\n")
    st.markdown("******")
    
    st.write("Contributor : [Akshat Kumar Nautiyal, Shivam Bhandari, Kaustubh Kukreti]")
    
    
if __name__ == '__main__':
    main()
