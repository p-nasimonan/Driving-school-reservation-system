import { initializeApp } from 'firebase/app';
import { getAuth } from 'firebase/auth';
import { getFirestore } from 'firebase/firestore';
import { getStorage } from 'firebase/storage';

// Firebaseの初期化
const firebaseConfig = {
  apiKey: "AIzaSyC5EY78xTBrdPZJc0-s82QfxfuQ0uZMfxQ",
  authDomain: "dsr-auto-system.firebaseapp.com",
  projectId: "dsr-auto-system",
  storageBucket: "dsr-auto-system.firebasestorage.app",
  messagingSenderId: "318566212020",
  appId: "1:318566212020:web:12f3d50fb1c0add582d2e1",
  measurementId: "G-SNTEC7LTEC"
};

const app = initializeApp(firebaseConfig);
const auth = getAuth(app);
const db = getFirestore(app);
const storage = getStorage(app);

export { auth, db, storage };