// GoogleLoginButton.js
import React from 'react';
import { auth, db} from './firebase';

const GoogleLoginButton = () => {
  const handleGoogleLogin = async () => {
    const provider = new auth.GoogleAuthProvider();
    try {
      const result = await auth.signInWithPopup(provider);
      const user = result.user;
      
      // 初回ログインの際にユーザー情報をFirestoreに保存
      if (user) {
        const userRef = db.collection('users').doc(user.uid);
        const doc = await userRef.get();
        if (!doc.exists) {
          await userRef.set({
            number: '',  // 初期値
            password: '',  // 初期値
            reservationSettings: {}  // 初期値
          });
        }
      }
    } catch (error) {
      console.error("Googleログインエラー:", error);
    }
  };

  return <button onClick={handleGoogleLogin}>Googleでログイン</button>;
};

export default GoogleLoginButton;
