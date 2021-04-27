/**
 * Sample React Native App
 * https://github.com/facebook/react-native
 *
 * @format
 * @flow strict-local
 */

 import React from 'react';
 import AppRouter from './AppRouter'
 import TTS from './AI/TextToSpeech'
 import PTT from './AI/SpeechToText'
 
 export default function App() {
   return (
      <PTT/>
      // <AppRouter/>
   );
 }
 