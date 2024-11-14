import React from 'react';
import GoogleLoginButton from './GoogleLoginButton';
import UserSettings from './UserSettings';
import { auth, firestore } from './firebase';


const App = () => {
  return (
    <div>
      <h1>ユーザー設定アプリ</h1>
      <GoogleLoginButton />
      <UserSettings />
    </div>
  );
};

export default App;
