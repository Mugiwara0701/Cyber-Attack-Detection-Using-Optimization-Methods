import numpy as np
import pickle
import streamlit as st


# loading the saved model 
loaded_model = pickle.load(open("D:/CYBER ATTACK DETECTION PROJECT/DETECTION SYSTEM (MODEL DEPLOYMENT)/trained_model.pkl",'rb'))

# creating a function for detection 

def attack_detection(input_data):
    
    
    # changing data to numpy array 
    input_data_array = np.asarray(input_data)
    
    # reshape the array as we are detection for one instance
    input_data_reshaped =  input_data_array.reshape(1,-1)
    
    result = loaded_model.predict(input_data_reshaped)
    print("The prediction is : ",result)
    
    if (result[0] == 'Benign'):
      return "NO ATTACK HAVE BEEN FOUND"
    else:
      return "ATTACK HAVE BEEN FOUND"
  

def main():
    # giving a title 
    st.markdown("<h1 style='text-align: center; color: blue;'>Cyber Attack Detection</h1>", unsafe_allow_html=True)
    
    # getting the input data from input user
    duration = st.text_input("Input the duration  : ")
    orig_bytes = st.text_input("Input the Orignal bytes : ")
    resp_bytesc = st.text_input("Input the response bytes : ")
    missed_bytes = st.text_input("Input the missed bytes : ")
    orig_pkts = st.text_input("Input the orignal packets: ")
    orig_ip_bytes = st.text_input("Input the orignal ip bytes : ")
    resp_pkts = st.text_input("Input the response packets : ")
    resp_ip_bytes= st.text_input("Input the respnose ip bytes: ")
    misses_bytes = st.text_input("Input the missing bytes : ")
    proto_icmp = st.text_input("Input the ICMP : ")
    proto_tcp = st.text_input("Input the TCP : ")
    proto_udp = st.text_input("Input the UDP : ")
    conn_state_OTH = st.text_input("Input the Connection state OTH: ")
    conn_state_REJ= st.text_input("Input the Connection state REJ : ")
    conn_state_RSTO = st.text_input("Input the Connection state RSTO: ")
    conn_state_RSTOS0 = st.text_input("Input the Connection state RSTOS0 : ")
    conn_state_RSTR = st.text_input("Input the Connection state RSTR : ")
    conn_state_RSTRH = st.text_input("Input the Connection state RSTRH: ")
    conn_state_S0 = st.text_input("Input the Connection state S0: ")
    conn_state_S1 = st.text_input("Input the Connection state S1: ")
    conn_state_S2 = st.text_input("Input the Connection state S2: ")
    conn_state_S3 = st.text_input("Input the Connection state S3: ")
    conn_state_SF = st.text_input("Input the Connection state SF: ")

    conn_state_SH = st.text_input("Input the Connection state SH: ")
    conn_state_SHR = st.text_input("Input the Connection state SHR: ")


    # code for prediction 
    detect = '' # null string 
    
    # creating a button for detection 
    
    if st.button('Input Test Result'):
        detect = attack_detection([duration, orig_bytes, resp_bytesc,missed_bytes,orig_pkts,orig_ip_bytes,resp_pkts,resp_ip_bytes,misses_bytes,proto_icmp,proto_tcp,proto_udp,conn_state_OTH,conn_state_REJ,conn_state_RSTO,conn_state_RSTOS0,conn_state_RSTR,conn_state_RSTRH,conn_state_S0, conn_state_S1,conn_state_S2, conn_state_S3, conn_state_SF, conn_state_SH, conn_state_SHR])
        
    st.success(detect)
    
    st.markdown("***")
    st.markdown(""" Connection state info:
    
    S0: Connection attempt seen, no reply yet\n
    S1: Connection established, not terminated\n
    S2: Client sents a SYN packet but not recive any ACK from server\n
    S3: Connection established of a TCP connection\n
    SF: Normal establishment and termination\n
    REJ: Connection attempt rejected\n
    RSTO: Connection established, originator aborted (sent a RST)\n
    RSTR: Connection established, responder aborted (sent a RST)\n
    RSTOS0: Originator sent a SYN followed by a RST, no response from responder\n
    RSTRH: Responder sent a SYN ACK followed by a RST, no response from originator\n
    SHR: Same as SYN_SENT (connection attempt initiated, not yet established)\n
    OTH: No SYN seen, just midstream traffic (often used to indicate a partial connection attempt)
    """)
    
    
    st.text("\n\n")
    st.markdown("<h3 style='text-align: center; color: blue;'>Model accuracy is 94% </h3>", unsafe_allow_html=True)
    
    
    st.write(" \n\n\n\n\n\n")
    st.markdown("******")
    
    st.write("Contributor : [Akshat Kumar Nautiyal, Shivam Bhandari, Kaustubh Kukreti]")
    
    
if __name__ == '__main__':
    main()