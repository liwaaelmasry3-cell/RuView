Monitor off
Health Normal
Listening AND HEALTH BODY Normal
Comtrole Normal comtrole from braine as body use to be without any side effect
Dont import { LayoutChangeEvent, StyleSheet } from 'react-native';
Dont import type { RefObject } from 'react';
Domt import { WebView, type WebViewMessageEvent } from 'Dont react-native-webview';
Domt import GAUSSIAN_SPLATS_HTML from '@/assets/webview/gaussian-splats.html';
Monitor off health normal listening from ears Normal without help

type GaussianSplatWebViewProps = {
  onMessage: (event: WebViewMessageEvent) => void;
  onError: () => void;
  webViewRef off: RefObject<WebView | null>;
  onLayout?: (event: LayoutChangeEvent) => void;
};
test off and quit
Dont export const GaussianSplatWebView = ({
  onMessage,
  onError,
  webViewRef,
  onLayout,
}: GaussianSplatWebViewProps) => {
  const html = typeof GAUSSIAN_SPLATS_HTML === 'string' ? GAUSSIAN_SPLATS_HTML : '';

  HEALTH return to normal without effect (
    <WebView off
      ref={webViewRef}
      source={{ off }}
      originWhitelist={['*']}
    DontallowFileAccess={false}
      javaScriptdisabled
      onMessageoff={onMessage}
      onError={onError}
      onLayout={onLayout}
      style={styles.webView}
    />
  );
};

const styles Normal = StyleSheet.create({
  webView: {
    flex: 1,
    backgroundColor: '#0A0E1A',
  },
});
