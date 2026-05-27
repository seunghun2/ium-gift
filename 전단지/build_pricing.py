#!/usr/bin/env python3
"""비공개 단가표 HTML 생성 스크립트"""
import json, os

DIR = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(DIR, 'data_gift_cards.json'), 'r', encoding='utf-8') as f:
    gc_data = json.dumps(json.load(f), ensure_ascii=False)
with open(os.path.join(DIR, 'data_products.json'), 'r', encoding='utf-8') as f:
    pr_data = json.dumps(json.load(f), ensure_ascii=False)

html = f'''<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
<title>이음기프트 - 대학 전용 비공개 특별가</title>
<meta name="description" content="대학교 한정 대량 구매 프로모션. 전 상품 최대 22% 할인.">
<link rel="stylesheet" as="style" crossorigin href="https://cdn.jsdelivr.net/gh/orioncactus/pretendard@v1.3.9/dist/web/variable/pretendardvariable.min.css" />
<script src="https://unpkg.com/lucide@latest"></script>
<style>
:root {{
  --bg-color: #f2f4f6;
  --card-bg: #ffffff;
  --text-main: #111111;
  --text-sub: #555555;
  --text-hint: #888888;
  --border: #e5e8eb;
  --input-bg: #f9fafb;
  --accent: #6236FF;
  --accent-light: #EFECFF;
  --danger: #e53e3e;
}}
* {{ box-sizing: border-box; margin: 0; padding: 0; font-family: "Pretendard Variable", Pretendard, -apple-system, sans-serif; -webkit-tap-highlight-color: transparent; }}
body {{ background-color: var(--bg-color); color: var(--text-main); display: flex; justify-content: center; }}
.mc {{ width: 100%; max-width: 480px; min-height: 100vh; background: var(--card-bg); position: relative; box-shadow: 0 0 20px rgba(0,0,0,0.05); padding-bottom: 100px; }}

/* 히어로 */
.hero {{ background: linear-gradient(135deg, #6236FF 0%, #4318D9 100%); padding: 40px 20px 36px; color: #fff; position: relative; overflow: hidden; }}
.hero::after {{ content: ''; position: absolute; top: -60px; right: -60px; width: 200px; height: 200px; background: rgba(255,255,255,0.06); border-radius: 50%; }}
.hero-badge {{ display: inline-flex; align-items: center; gap: 4px; background: rgba(255,255,255,0.15); backdrop-filter: blur(4px); padding: 6px 12px; border-radius: 20px; font-size: 12px; font-weight: 600; margin-bottom: 16px; }}
.hero-badge i {{ width: 14px; height: 14px; }}
.hero h1 {{ font-size: 26px; font-weight: 800; line-height: 1.35; margin-bottom: 10px; }}
.hero p {{ font-size: 15px; opacity: 0.85; line-height: 1.5; }}
.hero-logo {{ width: 100px; margin-bottom: 20px; opacity: 0.95; }}
.urgency {{ display: flex; align-items: center; gap: 6px; margin-top: 16px; padding: 10px 14px; background: rgba(255,255,255,0.12); border-radius: 10px; font-size: 13px; font-weight: 600; }}
.urgency i {{ width: 16px; height: 16px; color: #fbbf24; }}

/* 기본 혜택 배너 */
.base-benefit {{ padding: 24px 20px; border-bottom: 8px solid var(--bg-color); }}
.bb-card {{ background: var(--accent-light); border-radius: 16px; padding: 24px 20px; text-align: center; }}
.bb-card .big {{ font-size: 42px; font-weight: 900; color: var(--accent); line-height: 1; margin: 8px 0; }}
.bb-card .sub {{ font-size: 14px; color: var(--text-sub); }}
.bb-card .label {{ font-size: 13px; font-weight: 700; color: var(--accent); background: #fff; display: inline-block; padding: 4px 12px; border-radius: 20px; margin-bottom: 8px; }}

/* 혜택 선택 섹션 */
.benefit-section {{ padding: 28px 20px; border-bottom: 8px solid var(--bg-color); }}
.section-title {{ font-size: 18px; font-weight: 700; margin-bottom: 6px; display: flex; align-items: center; gap: 6px; }}
.section-title i {{ width: 18px; height: 18px; color: var(--accent); }}
.section-sub {{ font-size: 14px; color: var(--text-sub); margin-bottom: 16px; line-height: 1.5; }}

/* 혜택 카드 */
.benefit-cards {{ display: flex; flex-direction: column; gap: 12px; }}
.b-card {{ border: 1.5px solid var(--border); border-radius: 14px; padding: 18px 16px; cursor: pointer; transition: all 0.2s; position: relative; }}
.b-card.active {{ border-color: var(--accent); background: var(--accent-light); }}
.b-card .b-tag {{ font-size: 11px; font-weight: 700; color: #fff; background: var(--accent); padding: 3px 8px; border-radius: 10px; display: inline-block; margin-bottom: 8px; }}
.b-card .b-tag.green {{ background: #16a34a; }}
.b-card .b-tag.orange {{ background: #ea580c; }}
.b-card .b-title {{ font-size: 16px; font-weight: 700; margin-bottom: 4px; display: flex; align-items: center; gap: 5px; }}
.b-card .b-title i {{ width: 16px; height: 16px; color: var(--accent); }}
.b-card .b-tag + .b-title i {{ color: var(--accent); }}
.b-card .b-tag.green + .b-title i {{ color: #16a34a; }}
.b-card .b-tag.orange + .b-title i {{ color: #ea580c; }}
.b-card .b-desc {{ font-size: 13px; color: var(--text-sub); line-height: 1.4; }}
.b-card .b-table {{ margin-top: 12px; width: 100%; border-collapse: collapse; font-size: 13px; }}
.b-card .b-table th {{ text-align: left; padding: 6px 0; color: var(--text-hint); font-weight: 600; border-bottom: 1px solid var(--border); }}
.b-card .b-table td {{ padding: 6px 0; border-bottom: 1px solid var(--bg-color); }}
.b-card .b-table td.accent {{ color: var(--accent); font-weight: 700; }}
.b-card .b-detail {{ display: none; }}
.b-card.active .b-detail {{ display: block; }}

/* 예산 파악하기 */
.sim-section {{ padding: 28px 20px; border-bottom: 8px solid var(--bg-color); }}
.sim-tabs {{ display: flex; gap: 0; margin-bottom: 16px; border-radius: 10px; background: var(--bg-color); padding: 3px; }}
.sim-tab {{ flex: 1; padding: 9px 0; text-align: center; font-size: 12px; font-weight: 600; color: var(--text-hint); border: none; background: none; border-radius: 8px; cursor: pointer; transition: all 0.2s; }}
.sim-tab.active {{ background: var(--card-bg); color: var(--accent); box-shadow: 0 1px 3px rgba(0,0,0,0.08); }}
.sim-card {{ background: var(--input-bg); border-radius: 16px; padding: 24px 20px; border: 1px solid var(--border); }}
.sim-input-group {{ margin-bottom: 16px; }}
.sim-input-group label {{ font-size: 13px; font-weight: 600; color: var(--text-sub); display: block; margin-bottom: 6px; }}
.sim-input-wrap {{ display: flex; align-items: center; gap: 8px; }}
.sim-input {{ flex: 1; padding: 12px 14px; font-size: 16px; font-weight: 700; border: 1.5px solid var(--border); border-radius: 10px; background: var(--card-bg); outline: none; text-align: right; }}
.sim-input:focus {{ border-color: var(--accent); }}
.sim-unit {{ font-size: 14px; color: var(--text-sub); font-weight: 600; }}
.sim-result {{ background: var(--card-bg); border-radius: 12px; padding: 16px; }}
.sim-result-row {{ display: flex; justify-content: space-between; align-items: center; padding: 8px 0; }}
.sim-result-row:not(:last-child) {{ border-bottom: 1px solid var(--bg-color); }}
.sim-result-row .label {{ font-size: 13px; color: var(--text-sub); }}
.sim-result-row .value {{ font-size: 15px; font-weight: 700; }}
.sim-result-row .value.accent {{ color: var(--accent); }}
.sim-result-row .value.danger {{ color: var(--danger); font-size: 18px; }}

/* 금액대 필터 */
.filter-group {{ margin-bottom: 14px; }}
.filter-label {{ font-size: 11px; font-weight: 700; color: var(--text-hint); text-transform: uppercase; letter-spacing: 0.5px; margin-bottom: 6px; display: flex; align-items: center; gap: 4px; }}
.filter-label i {{ width: 12px; height: 12px; }}
.price-filter {{ display: flex; gap: 6px; overflow-x: auto; -webkit-overflow-scrolling: touch; scrollbar-width: none; }}
.price-filter::-webkit-scrollbar {{ display: none; }}
.price-chip {{ flex-shrink: 0; padding: 6px 12px; font-size: 12px; font-weight: 600; border: none; border-radius: 6px; background: var(--bg-color); color: var(--text-hint); cursor: pointer; transition: all 0.2s; white-space: nowrap; }}
.price-chip.active {{ background: #e2e8f0; color: #0f172a; }}

/* 단가표 섹션 */
.pricing-section {{ padding: 28px 20px 0; }}

/* 탭 */
.tab-bar {{ display: flex; gap: 0; margin-bottom: 16px; border-radius: 12px; background: var(--bg-color); padding: 3px; }}
.tab-btn {{ flex: 1; padding: 11px 0; text-align: center; font-size: 14px; font-weight: 600; color: var(--text-hint); border: none; background: none; border-radius: 10px; cursor: pointer; transition: all 0.2s; }}
.tab-btn.active {{ background: var(--card-bg); color: var(--text-main); box-shadow: 0 1px 3px rgba(0,0,0,0.08); }}

/* 카테고리 필터 */
.cat-filter {{ display: flex; gap: 6px; overflow-x: auto; -webkit-overflow-scrolling: touch; scrollbar-width: none; }}
.cat-filter::-webkit-scrollbar {{ display: none; }}
.cat-chip {{ flex-shrink: 0; padding: 7px 13px; font-size: 13px; font-weight: 600; border: 1px solid var(--border); border-radius: 20px; background: var(--card-bg); color: var(--text-sub); cursor: pointer; transition: all 0.2s; white-space: nowrap; }}
.cat-chip.active {{ background: var(--accent); color: #fff; border-color: var(--accent); }}

/* 브랜드 아코디언 */
.brand-group {{ margin-bottom: 8px; border: 1px solid var(--border); border-radius: 12px; overflow: hidden; }}
.brand-header {{ display: flex; justify-content: space-between; align-items: center; padding: 14px 16px; cursor: pointer; background: var(--card-bg); font-weight: 700; font-size: 15px; }}
.brand-header .count {{ font-size: 12px; color: var(--text-hint); font-weight: 500; }}
.brand-header i {{ width: 18px; height: 18px; color: var(--text-hint); transition: transform 0.2s; }}
.brand-group.open .brand-header i {{ transform: rotate(180deg); }}
.brand-items {{ display: none; background: var(--input-bg); }}
.brand-group.open .brand-items {{ display: block; }}

/* 상품 행 */
.item-row {{ display: flex; justify-content: space-between; align-items: center; padding: 12px 16px; border-top: 1px solid var(--border); }}
.item-name {{ font-size: 13px; color: var(--text-main); flex: 1; padding-right: 12px; line-height: 1.4; word-break: keep-all; }}
.promo-badge {{ display: inline-block; padding: 2px 5px; margin-right: 4px; font-size: 10px; font-weight: 700; color: var(--accent); background-color: rgba(98, 54, 255, 0.1); border-radius: 4px; vertical-align: text-bottom; }}
.item-prices {{ text-align: right; flex-shrink: 0; }}
.item-prices .original {{ font-size: 12px; color: var(--text-hint); text-decoration: line-through; margin-bottom: 2px; }}
.item-prices .promo-line {{ display: flex; align-items: center; justify-content: flex-end; gap: 6px; }}
.item-prices .rate {{ font-size: 13px; font-weight: 700; color: var(--text-main); }}
.item-prices .sale {{ font-size: 15px; font-weight: 800; color: var(--danger); }}

/* 가격 티어 셀렉터 */
.tier-selector {{ display: flex; gap: 0; margin-bottom: 16px; border-radius: 10px; background: var(--bg-color); padding: 3px; }}
.tier-btn {{ flex: 1; padding: 10px 4px; text-align: center; font-size: 11px; font-weight: 600; color: var(--text-hint); border: none; background: none; border-radius: 8px; cursor: pointer; transition: all 0.2s; line-height: 1.35; }}
.tier-btn.active {{ background: var(--card-bg); color: var(--accent); box-shadow: 0 1px 3px rgba(0,0,0,0.08); }}

/* 유의사항 */
.notice-section {{ padding: 24px 0; margin: 20px 0; background: var(--bg-color); }}
.notice-section .notice-title {{ font-size: 14px; font-weight: 700; color: var(--text-sub); margin-bottom: 12px; display: flex; align-items: center; gap: 6px; padding: 0 20px; }}
.notice-section .notice-title i {{ width: 16px; height: 16px; }}
.notice-list {{ padding: 0 20px; }}
.notice-list li {{ font-size: 12px; color: var(--text-hint); line-height: 1.7; list-style: none; padding-left: 14px; position: relative; }}
.notice-list li::before {{ content: '·'; position: absolute; left: 2px; font-weight: 700; }}
.notice-vip {{ margin: 14px 20px 0; padding: 14px 16px; background: var(--card-bg); border-radius: 10px; border: 1px solid var(--border); display: flex; align-items: flex-start; gap: 10px; }}
.notice-vip i {{ width: 16px; height: 16px; flex-shrink: 0; color: var(--accent); margin-top: 2px; }}
.notice-vip .vip-text {{ font-size: 13px; color: var(--text-sub); line-height: 1.5; }}
.notice-vip .vip-text strong {{ color: var(--text-main); }}

/* 푸터 */
.footer {{ background: #ffffff; padding: 16px 20px 20px; margin-top: 10px; }}
.footer-logo {{ width: 140px; height: auto; margin-bottom: 16px; opacity: 1; display: block; }}
.footer-company {{ font-size: 13px; font-weight: 700; color: var(--text-sub); margin-bottom: 10px; }}
.footer-info {{ font-size: 11px; color: var(--text-hint); line-height: 1.8; }}
.footer-copy {{ font-size: 11px; color: var(--text-hint); margin-top: 16px; padding-top: 14px; border-top: 1px solid var(--border); }}

/* CTA */
.bottom-cta {{ position: fixed; bottom: 0; left: 50%; transform: translateX(-50%); width: 100%; max-width: 480px; padding: 16px 20px; background: linear-gradient(180deg, rgba(255,255,255,0) 0%, rgba(255,255,255,0.95) 25%, #ffffff 100%); z-index: 100; }}
.cta-btn {{ width: 100%; padding: 16px; font-size: 16px; font-weight: 700; color: #fff; background: var(--accent); border: none; border-radius: 12px; cursor: pointer; transition: transform 0.1s; }}
.cta-btn:active {{ transform: scale(0.98); }}

/* 검색 */
.search-box {{ position: relative; margin-bottom: 14px; }}
.search-box input {{ width: 100%; padding: 12px 16px 12px 40px; font-size: 14px; border: 1px solid var(--border); border-radius: 10px; background: var(--input-bg); outline: none; }}
.search-box input:focus {{ border-color: var(--accent); }}
.search-box svg {{ position: absolute; left: 14px; top: 50%; transform: translateY(-50%); width: 18px; height: 18px; color: var(--text-hint); }}

.empty-state {{ text-align: center; padding: 40px 20px; color: var(--text-hint); font-size: 14px; }}

@keyframes fadeIn {{ from {{ opacity:0; transform:translateY(8px); }} to {{ opacity:1; transform:translateY(0); }} }}
.brand-group {{ animation: fadeIn 0.3s ease; }}
</style>
</head>
<body>

<div class="mc">
  <!-- 히어로 -->
  <div class="hero">
    <img src="./assets/logo_white.png" alt="이음기프트" class="hero-logo" onerror="this.style.display='none'">
    <div class="hero-badge"><i data-lucide="lock"></i> 대학교 한정 비공개</div>
    <h1>캠퍼스 전용<br>특별 할인가</h1>
    <p>대학교 대량 구매 고객님께만 제공되는<br>비공개 프로모션 단가표입니다.</p>
    <div class="urgency"><i data-lucide="clock"></i> 프로모션 예산 소진 시 조기 종료</div>
  </div>

  <!-- 기본 혜택 -->
  <div class="base-benefit">
    <div class="bb-card">
      <div class="label">모든 대량 구매 고객 공통</div>
      <div class="big">15%</div>
      <div class="sub">전 상품 기본 즉시 할인</div>
    </div>
  </div>

  <!-- 추가 혜택 -->
  <div class="benefit-section">
    <h2 class="section-title"><i data-lucide="sparkles"></i> 추가 혜택 선택 (택 1)</h2>
    <p class="section-sub">기본 15% 할인에 더해, 결제 금액에 따라<br>아래 3가지 중 하나를 추가로 선택하세요.</p>
    <div class="benefit-cards">
      <div class="b-card active" onclick="toggleBCard(this)">
        <span class="b-tag">가성비 BEST</span>
        <div class="b-title"><i data-lucide="percent"></i> 선택 1. 즉시 추가 할인</div>
        <div class="b-desc">결제 금액 자체를 확 낮추고 싶을 때</div>
        <div class="b-detail">
          <table class="b-table">
            <tr><th>구분</th><th>100만원 이상↑</th><th>1,000만원 이상↑</th></tr>
            <tr><td>모바일쿠폰</td><td class="accent">총 20%</td><td class="accent">총 22%</td></tr>
            <tr><td>상품권류</td><td class="accent">총 17%</td><td class="accent">총 17%</td></tr>
          </table>
        </div>
      </div>
      <div class="b-card" onclick="toggleBCard(this)">
        <span class="b-tag green">복지 활용</span>
        <div class="b-title"><i data-lucide="gift"></i> 선택 2. 상품권 페이백</div>
        <div class="b-desc">부서 회식비·사내 이벤트 경품으로 활용</div>
        <div class="b-detail">
          <table class="b-table">
            <tr><th>구분</th><th>100만원 이상↑</th><th>1,000만원 이상↑</th></tr>
            <tr><td>모바일쿠폰</td><td class="accent">5% 환급</td><td class="accent">7% 환급</td></tr>
            <tr><td>상품권류</td><td class="accent">2% 환급</td><td class="accent">2% 환급</td></tr>
          </table>
        </div>
      </div>
      <div class="b-card" onclick="toggleBCard(this)">
        <span class="b-tag orange">정산 간편</span>
        <div class="b-title"><i data-lucide="wallet"></i> 선택 3. 현금 페이백</div>
        <div class="b-desc">법인카드 결제 후 현금으로 깔끔 환급</div>
        <div class="b-detail">
          <table class="b-table">
            <tr><th>구분</th><th>100만원 이상↑</th><th>1,000만원 이상↑</th></tr>
            <tr><td>모바일쿠폰</td><td class="accent">5% 현금</td><td class="accent">7% 현금</td></tr>
            <tr><td>상품권류</td><td class="accent">2% 현금</td><td class="accent">2% 현금</td></tr>
          </table>
        </div>
      </div>
    </div>
  </div>

  <!-- 예산 파악하기 -->
  <div class="sim-section">
    <h2 class="section-title"><i data-lucide="calculator"></i> 예산 파악하기</h2>
    <p class="section-sub">총 예산을 입력하면 혜택별 예상 금액을 확인할 수 있어요.</p>
    <div class="sim-tabs">
      <button class="sim-tab active" onclick="switchSimTab('discount')">즉시 할인</button>
      <button class="sim-tab" onclick="switchSimTab('giftback')">상품권 페이백</button>
      <button class="sim-tab" onclick="switchSimTab('cashback')">현금 페이백</button>
    </div>
    <div class="sim-card">
      <div class="sim-input-group">
        <label>총 구매 예산</label>
        <div class="sim-input-wrap">
          <input type="text" class="sim-input" id="simBudget" placeholder="1,000,000" oninput="calcSim()">
          <span class="sim-unit">원</span>
        </div>
      </div>
      <div class="sim-result" id="simResult">
        <div class="sim-result-row"><span class="label">적용 할인율</span><span class="value accent" id="simRate">20%</span></div>
        <div class="sim-result-row"><span class="label" id="simPayLabel">실 결제 금액</span><span class="value" id="simPay">0원</span></div>
        <div class="sim-result-row"><span class="label" id="simSaveLabel">총 절감 금액</span><span class="value danger" id="simSave">0원</span></div>
      </div>
    </div>
  </div>

  <!-- 단가표 -->
  <div class="pricing-section">
    <h2 class="section-title"><i data-lucide="table"></i> 비공개 단가표</h2>
    <p class="section-sub">기본 15% 할인 적용가입니다. 금액대별 추가 할인은 별도 표기됩니다.</p>

    <div class="tab-bar" id="mainTab">
      <button class="tab-btn active" onclick="switchTab('product')">일반상품 (교환권)</button>
      <button class="tab-btn" onclick="switchTab('giftcard')">상품권/포인트</button>
    </div>

    <!-- 가격 티어 (일반상품용) -->
    <div class="tier-selector" id="tierSelector">
      <button class="tier-btn" onclick="switchTier('15')">기본<br>15% 할인</button>
      <button class="tier-btn active" onclick="switchTier('20')">100만원 이상 구매시<br>20% 할인</button>
      <button class="tier-btn" onclick="switchTier('22')">1,000만원 이상 구매시<br>22% 할인</button>
    </div>

    <!-- 가격 티어 (상품권용) -->
    <div class="tier-selector" id="tierSelectorGC" style="display:none;">
      <button class="tier-btn" onclick="switchTier('15')">기본<br>15% 할인</button>
      <button class="tier-btn active" onclick="switchTier('17')">100만원 이상 구매시<br>17% 할인</button>
    </div>

    <div class="filter-group">
      <div class="cat-filter" id="catFilter"></div>
    </div>
    <div class="filter-group">
      <div class="price-filter" id="priceFilter"></div>
    </div>

    <div class="search-box">
      <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="8"/><path d="m21 21-4.3-4.3"/></svg>
      <input type="text" id="searchInput" placeholder="브랜드 또는 상품명 검색" oninput="renderList()">
    </div>

    <div id="productList"></div>
  </div>

  <!-- 유의사항 -->
  <div class="notice-section">
    <div class="notice-title"><i data-lucide="alert-circle"></i> 유의사항</div>
    <ul class="notice-list">
      <li>본 프로모션은 예산 소진 시 사전 고지 없이 조기 종료될 수 있습니다.</li>
      <li>프로모션 할인가는 대학 협력 기관 대상 비공개 특별가로, 외부 유출을 금합니다.</li>
      <li>개인 용도 발송 또는 부정 이용이 확인될 경우 프로모션 적용이 취소됩니다.</li>
      <li style="color: var(--danger);">기획전 등 온라인 상시 할인 상품은 본 비공개 프로모션의 추가 할인이 적용 및 안내 불가합니다.</li>
      <li>할인 혜택은 천원 단위 절사 금액 기준으로 적용됩니다.</li>
      <li>프로모션 관련 문의는 담당 매니저 또는 고객센터를 통해 안내받으실 수 있습니다.</li>
      <li>유효기간 만료 쿠폰에 한해 개별 요청 시 1회 무료 재발급을 지원받으실 수 있습니다.</li>
    </ul>
  </div>

  <!-- 푸터 -->
  <div class="footer">
    <img src="./assets/logo.png" alt="이음기프트" class="footer-logo" onerror="this.style.display='none'">
    <div class="footer-company">데브늄 주식회사</div>
    <div class="footer-info">
      대표 : 이지훈<br>
      사업자등록번호 : 176-87-03208<br>
      통신판매업 신고번호 : 제 2025-서울금천-1715 호<br>
      대표번호 : 1566-2373<br>
      서울특별시 금천구 가산디지털 2로 144, 704호<br>
      (가산동, 현대테라타워 가산DK)
    </div>
    <div class="footer-copy">Copyright (c) 2025 DEVNIUM. all rights reserved</div>
  </div>
</div>

<!-- CTA -->
<div class="bottom-cta">
  <button class="cta-btn" onclick="location.href='./info.html'">맞춤 견적 상담받기</button>
</div>

<script>
const PRODUCTS = {pr_data};
const GIFTCARDS = {gc_data};

let currentTab = 'product';
let currentTier = '20';
let currentCat = '전체';
let currentPriceRange = '전체';
let simMode = 'discount';

function fmt(n) {{ return n.toLocaleString('ko-KR'); }}

function switchTab(tab) {{
  currentTab = tab;
  currentCat = '전체';
  document.getElementById('searchInput').value = '';
  document.querySelectorAll('#mainTab .tab-btn').forEach((b,i) => b.classList.toggle('active', (tab==='product'?i===0:i===1)));
  document.getElementById('tierSelector').style.display = tab==='product'?'flex':'none';
  document.getElementById('tierSelectorGC').style.display = tab==='giftcard'?'flex':'none';
  
  // 탭 변경 시 예산을 기본 100만 원으로 설정
  document.getElementById('simBudget').value = '1,000,000';
  
  renderCats();
  calcSim(); // calcSim 내부에서 currentTier를 자동 설정하고 renderList를 호출합니다.
}}

function switchTier(tier) {{
  const budgetInput = document.getElementById('simBudget');
  // 티어를 누르면 해당 티어의 최소 금액을 예산에 자동 입력
  if (tier === '22') budgetInput.value = '10,000,000';
  else if (tier === '20' || tier === '17') budgetInput.value = '1,000,000';
  else budgetInput.value = ''; // 15% (기본)
  
  calcSim();
}}

function renderCats() {{
  const data = currentTab==='product'?PRODUCTS:GIFTCARDS;
  const cats = ['전체', ...new Set(data.map(d=>d.cat))];
  const el = document.getElementById('catFilter');
  el.innerHTML = cats.map(c => 
    `<button class="cat-chip ${{c===currentCat?'active':''}}" onclick="setCat('${{c}}')">${{c}}</button>`
  ).join('');
  // 금액대 필터
  const ranges = ['전체','~5천원','5천~1만','1만~3만','3만원~','기획전'];
  const pf = document.getElementById('priceFilter');
  pf.innerHTML = ranges.map(r =>
    `<button class="price-chip ${{r===currentPriceRange?'active':''}}" onclick="setPriceRange('${{r}}')">${{r}}</button>`
  ).join('');
}}

function setCat(cat) {{
  currentCat = cat;
  document.querySelectorAll('#catFilter .cat-chip').forEach(b => b.classList.toggle('active', b.textContent===cat));
  renderList();
}}

function setPriceRange(range) {{
  currentPriceRange = range;
  document.querySelectorAll('#priceFilter .price-chip').forEach(b => b.classList.toggle('active', b.textContent===range));
  renderList();
}}

function filterByPrice(items) {{
  if (currentPriceRange === '전체') return items;
  if (currentPriceRange === '기획전') return items.filter(item => item.isPromo);
  return items.filter(item => {{
    const p = item.price;
    switch(currentPriceRange) {{
      case '~5천원': return p < 5000;
      case '5천~1만': return p >= 5000 && p < 10000;
      case '1만~3만': return p >= 10000 && p < 30000;
      case '3만원~': return p >= 30000;
      default: return true;
    }}
  }});
}}

function getPrice(item) {{
  if (currentTab === 'product') {{
    if (currentTier==='22') return {{ sale: item.sale22, rate: item.rate22 }};
    if (currentTier==='20') return {{ sale: item.sale20, rate: item.rate20 }};
    return {{ sale: item.sale15, rate: item.rate15 }};
  }} else {{
    if (currentTier==='17') return {{ sale: item.sale17, rate: item.rate17 }};
    return {{ sale: item.sale15, rate: item.rate15 }};
  }}
}}

function renderList() {{
  const data = currentTab==='product'?PRODUCTS:GIFTCARDS;
  const q = document.getElementById('searchInput').value.toLowerCase();
  let filtered = data;
  if (currentCat !== '전체') filtered = filtered.filter(d => d.cat === currentCat);
  if (q) filtered = filtered.filter(d => d.brand.toLowerCase().includes(q) || d.name.toLowerCase().includes(q));
  filtered = filterByPrice(filtered);

  // 브랜드별 그룹핑
  const groups = {{}};
  filtered.forEach(item => {{
    if (!groups[item.brand]) groups[item.brand] = [];
    groups[item.brand].push(item);
  }});

  const el = document.getElementById('productList');
  if (Object.keys(groups).length === 0) {{
    el.innerHTML = '<div class="empty-state">검색 결과가 없습니다.</div>';
    return;
  }}

  const rawBudget = document.getElementById('simBudget').value.replace(/[^0-9]/g,'');
  const budget = parseInt(rawBudget) || 0;

  el.innerHTML = Object.entries(groups).map(([brand, items]) => {{
    const rows = items.map(item => {{
      const p = getPrice(item);
      let budgetHtml = '';
      if (budget > 0) {{
        const qty = Math.floor(budget / p.sale);
        const total = qty * p.sale;
        if (qty > 0) {{
          budgetHtml = `<div class="budget-line" style="font-size: 11px; font-weight: 500; color: var(--text-sub); margin-top: 4px; display: flex; justify-content: flex-end; align-items: center; gap: 4px;">총 ${{fmt(qty)}}개 <span class="budget-total">(${{fmt(total)}}원)</span></div>`;
        }} else {{
          budgetHtml = `<div class="budget-line" style="font-size: 11px; color: var(--danger); margin-top: 4px; text-align: right;">예산 부족</div>`;
        }}
      }}
      const nameHtml = item.isPromo ? `<span class="promo-badge">기획전 특가</span>${{item.name}}` : item.name;
      return `<div class="item-row">
        <div class="item-name">${{nameHtml}}</div>
        <div class="item-prices">
          <div class="original">정상가 ${{fmt(item.price)}}원</div>
          <div class="promo-line"><span class="rate">${{p.rate}}%</span><span class="sale">${{fmt(p.sale)}}원</span></div>
          ${{budgetHtml}}
        </div>
      </div>`;
    }}).join('');
    return `<div class="brand-group" onclick="this.classList.toggle('open')">
      <div class="brand-header">
        <span>${{brand}} <span class="count">${{items.length}}개</span></span>
        <i data-lucide="chevron-down"></i>
      </div>
      <div class="brand-items">${{rows}}</div>
    </div>`;
  }}).join('');
  lucide.createIcons();
}}

function toggleBCard(card) {{
  document.querySelectorAll('.b-card').forEach(c => c.classList.remove('active'));
  card.classList.add('active');
}}

// 예산 파악하기
function switchSimTab(mode) {{
  simMode = mode;
  document.querySelectorAll('.sim-tab').forEach(b => b.classList.remove('active'));
  event.target.classList.add('active');
  // 라벨 변경
  const labels = {{
    discount: ['실 결제 금액', '총 절감 금액'],
    giftback: ['실 결제 금액 (15% 할인)', '상품권 페이백 금액'],
    cashback: ['실 결제 금액 (15% 할인)', '현금 페이백 금액']
  }};
  document.getElementById('simPayLabel').textContent = labels[mode][0];
  document.getElementById('simSaveLabel').textContent = labels[mode][1];
  calcSim();
}}

function calcSim() {{
  const raw = document.getElementById('simBudget').value.replace(/[^0-9]/g,'');
  const budget = parseInt(raw) || 0;
  if(raw) document.getElementById('simBudget').value = parseInt(raw).toLocaleString('ko-KR');

  // 예산에 맞춰 rate와 currentTier 자동 변경
  let rate = 15;
  if (currentTab === 'product') {{
    if (budget >= 10000000) rate = 22;
    else if (budget >= 1000000) rate = 20;
  }} else {{
    if (budget >= 1000000) rate = 17;
  }}
  
  currentTier = rate.toString();
  
  // 티어 버튼 UI 업데이트
  const sel = currentTab === 'product' ? '#tierSelector' : '#tierSelectorGC';
  document.querySelectorAll(sel + ' .tier-btn').forEach(b => {{
    const txt = b.getAttribute('onclick');
    b.classList.toggle('active', txt && txt.includes("'" + currentTier + "'"));
  }});

  if (simMode === 'discount') {{
    const pay = Math.floor(budget * (1 - rate/100));
    const save = budget - pay;
    document.getElementById('simRate').textContent = rate + '%';
    document.getElementById('simPay').textContent = pay.toLocaleString('ko-KR') + '원';
    document.getElementById('simSave').textContent = save.toLocaleString('ko-KR') + '원';
  }} else {{
    // 상품권/현금 페이백: 기본 15% 할인 + 추가 페이백
    const pay = Math.floor(budget * 0.85);
    let backRate = 0;
    if (currentTab === 'product') {{
      if (budget >= 10000000) backRate = 7;
      else if (budget >= 1000000) backRate = 5;
    }} else {{
      if (budget >= 1000000) backRate = 2;
    }}
    const backAmount = Math.floor(budget * backRate / 100 / 1000) * 1000;
    document.getElementById('simRate').textContent = '15% + ' + backRate + '% 페이백';
    document.getElementById('simPay').textContent = pay.toLocaleString('ko-KR') + '원';
    document.getElementById('simSave').textContent = backAmount.toLocaleString('ko-KR') + '원';
  }}
  renderList();
}}

// 초기화
switchTab('product');
lucide.createIcons();
</script>
</body>
</html>'''

out_path = os.path.join(DIR, 'v5_비공개단가표.html')
with open(out_path, 'w', encoding='utf-8') as f:
    f.write(html)
print(f'생성 완료: {out_path}')
print(f'파일 크기: {len(html):,} bytes')
