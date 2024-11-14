// UserSettings.js
import React, { useState } from 'react';
import { auth, db} from './firebase';

const UserSettings = () => {
  const [number, setNumber] = useState('');
  const [password, setPassword] = useState('');
  const [reservationSettings, setReservationSettings] = useState({});

  const handleSave = async () => {
    const user = auth.currentUser;
    if (user) {
      await db.collection('users').doc(user.uid).set({
        number,
        password,
        reservationSettings,
      }, { merge: true });
      alert("設定が保存されました");
    } else {
      alert("ログインが必要です");
    }
  };

  return (
    <div>
      <h2>ユーザー設定</h2>
      <label>
        教習生番号:
        <input type="text" value={number} onChange={(e) => setNumber(e.target.value)} />
      </label>
      <br />
      <label>
        パスワード:
        <input type="password" value={password} onChange={(e) => setPassword(e.target.value)} />
      </label>
      <br />
      <label>
        予約設定:
        <input type="text" value={JSON.stringify(reservationSettings)} onChange={(e) => setReservationSettings(JSON.parse(e.target.value))} />
      </label>
      <br />
      <button onClick={handleSave}>保存</button>
    </div>
  );
};

export default UserSettings;
