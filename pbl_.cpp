//mobile section  
  {
//---------label for mobiles      
 label1:
   if (gadgets==1)
  { cout<<"Plz enter your budget"<<endl;
   cin>>a;
   if(a>6000 && a<=7000)
   {cout<<"1)Redmi 9A sport (2GB Ram,32GB) @ Rs.6999\n2)samsung A03 (2GB Ram,32GB) @ Rs.6999";}
   else if(a>7000 && a<=8000)
   {cout<<"1)Realme C30 (2GB Ram,32 GB) @ Rs.7499\n2)Redmi 9A(2GB Ram,32GB) @ Rs.7499";}
   else if (a>8000 && a<=9000)
   {cout<<"1)realme Narzo 30A(3GB Ram,32GB)@ Rs.8999\n2)redmi 9i sport(4GB Ram,64GB)@Rs.8799";}
   else if(a>9000 && a<=10000)
   {cout<<"1)moto G22 (4GB Ram, 64GB) @ Rs.9999\n2)realme C31(3GB Ram, 32GB)@ Rs.9299\n3)oppo A15s(4GB Ram, 64GB) @ Rs.9990";}
   else if (a>10000 && a<=15000)
   {int t;
       cout<<"what are you looking for in that mobile\n1)Performance\n2)Battery backup\n3)Camera\n4)All Rounder";
       {cin>>t;
       if (t==1){cout<<"IQOO Z6 (4GB Ram,128GB)@ Rs.14499\n(SD 680, Amoled screen)";}
       else if (t==2){cout<<"1)poco M3(6GB Ram,64GB)@ Rs.10999\n(6000mAh)";}
       else if (t==3){cout<<"realme 9i(4GB Ram,64GB)@ Rs.10999\n(50 MP AI triple Camera)";}
       else if (t==4){cout<<"samsung A13(4GB Ram,64GB)@ Rs.13999\n(android 12,5000mAh)";}
       }
       
   }
   
  else if(a>15000 && a<=20000)
  {int t;
      cout<<"what are you looking for in that mobile\n1)Performance\n2)Camera\n3)All Rounder";
      cin>>t;
      if(t==1){cout<<"IQOO Z6 (8GB Ram,128GB) @ Rs.17999\n(SD 695 5G, 5000mAh)";}
      else if(t==2){cout<<"One plus nord CE2 lite (6GB Ram, 128G)@ Rs.18999\n(64 MP camera)";}
      else if(t==3){cout<<"Realme 9i 5G Speed Edition (8GB Ram, 128GB storage) @ Rs.19999\n(Snapdragon 778G 5G)\n(144 Hz display, 48 MP AI Camera)";}
  }
  else if(a>20000 && a<=25000)
  {int t;
  cout<<"what are you looking for in that mobile\n1)Performance\n2)Camera\n3)All Rounder";
  cin>>t;
     if(t==1){cout<<"Readmi Note 11 Pro Plus 5G (6GB,256GB) @Rs.24999";}
     else if (t==2){cout<<"realme 9 pro + 5G (8GB Ram,128GB) @ Rs.24999";}
     else if (t==3){cout<<"iQOO Z6 Pro 5G(8GB Ram,128GB storage) @ rs.24999\n(Snapdragon 778G 5G)\n(66W Flash charge)\n1300 nits peak brightness\nHDR 10+";}
  }
  else if(a>25000 && a<=30000)
 
  {int t;
  cout<<"what are you looking for in that mobile\n1)Performance\n2)Camera";
  cin>>t;
  if (t==1){cout<<"IQOO Neo 6 5G (8GB Ram,128GB storage) @ Rs.29999";}
  else if(t==2){cout<<"1)realme GT Master Edition (8GB,128GB storage) @ Rs.29990\n2)Oneplus nord 2 5g(8GB ram ,256 GB storage) @ 29999";}
  
  }

   else if(a>30000 && a<=40000)
   {
     cout<<"which OS you want 1)ios or 2)Android";
     int b;
     cin>>b;
     if(b==1){cout<<"iphone SE(64GB) @ 39999";}
     else if(b==2)
     {int t;
         cout<<"what are you looking for in that mobile\n1)Performance\n2)Camera\n3)All Rounder";
         cin>>t;
         if(t==1){cout<<"Mi 11T pro 5g(8GB Ram,128 Gb storage) @ Rs.37999";}
         else if(t==2){cout<<"IQOO 7 legend(8GB Ram,128 Gb storage) @ Rs.37990";}
         else if(t==3){cout<<"Oneplus 9RT(8GB Ram,128 Gb storage) @ Rs.39999";}
     }
   }
     else if(a>40000 && a<=47000)
     {int b;
      cout<<"which OS you want 1)ios or 2)Android";
     cin>>b;
         if(b==1){cout<<"iphone 12 (64GB) @ Rs.46999";}
         else if (b==2){cout<<"1)IQOO 9 (12GB, 256GB storage)@ Rs.45990\n2)oneplus 9(8GB Ram, 128GB storage) @ Rs.46999"; }
     }
     else if (a>47000 && a<=50000)
     {cout<<"1)realme GT 2 pro @ Rs.49999\n2)Oneplus 9 @ Rs.49999";}
     else if (a>50000)
     {cout<<"There are very specific options after Rs.50000 like in Ios\n1)iphone 13 min\n2)iphone 13\n3)iphone 13 pro\n4)iphone 13 pro max\n And in android\n1)Oneplus 10 pro\n2)samsung galaxy s22\n3)samsung s22 ultra\n4)samsung note 20 FE\n5)vivo x80 pro\n6)Xiomi 12s ultra\n7)IQOO 9 pro";}
   }