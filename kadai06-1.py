<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="utf-8">
<title>e‑Stat API サンプル</title>
</head>
<body>
  <h1>e‑Stat：都道府県別一次産業出荷額</h1>
  <button type="button" onclick="getStats()">取得実行</button>
  <div id="result" style="white-space: pre-wrap; margin-top:1em;"></div>

<script>
// ---
// e‑Stat API：都道府県別 一次産業出荷額（G03001：2015年実績）
// エンドポイントと機能：
// URL：https://api.e-stat.go.jp/rest/3.0/app/json/getStatsData
// → 指定コードの統計データを取得する汎用API :contentReference[oaicite:2]{index=2}
//
// パラメータ：
//   appId       : 自分の e‑Stat アプリケーションID
//   statsDataId : データセットID（例：G03001）
//   cdTab       : 都道府県を指定（例：01=北海道など）
//   lang        : "J"（日本語）
// レスポンス：
// JSON形式で返却。「STATISTICALDATA」→「STATISTICAL_DATA」下にデータ配列。
// 各レコードに属性：都道府県コード、年、値(value) など
// ---

async function getStats(){
  const appId = 'YOUR_APP_ID_HERE'; // ← 事前に e‑Stat から取得
  const statsDataId = '0003426389'; // G03001に相当するID
  const url = `https://api.e-stat.go.jp/rest/3.0/app/json/getStatsData?appId=${appId}&statsDataId=${statsDataId}&lang=J`;

  try{
    const resp = await fetch(url);
    const json = await resp.json();
    const data = json.GET_STATS_DATA.STATISTICAL_DATA.DATA_INF.VALUE;
    let text = '都道府県別 一次産業出荷額（円）\n';
    data.forEach(item => {
      const area = item["@area"];
      const year = item["@time"];
      const val = item["$"];
      text += `${year}年 地域 ${area}：${val} 円\n`;
    });
    document.getElementById('result').innerText = text;
  }catch(e){
    console.error(e);
    document.getElementById('result').innerText = '通信エラーまたは不正なレスポンスです。';
  }
}
</script>
</body>
</html>
