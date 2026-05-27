  
    lucide.createIcons();

    let currentStep = 0;
    const totalSteps = 8; // step1 ~ step8

    function updateProgress() {
      if (currentStep === 0 || currentStep === 9) {
        document.getElementById('progressWrap').style.display = 'none';
        document.getElementById('navBar').style.display = 'none';
      } else {
        document.getElementById('progressWrap').style.display = 'block';
        document.getElementById('navBar').style.display = 'flex';
        const percent = ((currentStep) / totalSteps) * 100;
        document.getElementById('progressBar').style.width = percent + '%';
      }
    }

    function showStep(stepNum) {
      document.querySelectorAll('.step-section').forEach((el, idx) => {
        el.classList.remove('active', 'prev');
        if (idx < stepNum) el.classList.add('prev');
        else if (idx === stepNum) el.classList.add('active');
      });
      currentStep = stepNum;
      updateProgress();

      // 자동 포커스
      setTimeout(() => {
        const activeInput = document.querySelector(`#step${stepNum} input[type="text"], #step${stepNum} input[type="tel"]`);
        if(activeInput) activeInput.focus();
      }, 400);
    }

    function startForm() {
      showStep(1);
    }

    function goNext() {
      let nextStep = currentStep + 1;
      
      // 소속구분(Step 4) 이후, 총무처/교무처가 아니면 파일첨부(Step 5) 건너뛰고 바로 부서명(Step 6)으로
      if (nextStep === 5 && formData['orgType'] !== '총무처/교무처') {
        nextStep = 6;
      }

      if(nextStep <= 8) {
        showStep(nextStep);
      }
    }

    function goPrev() {
      let prevStep = currentStep - 1;

      // 부서명(Step 6)에서 뒤로갈 때, 파일첨부를 안 거친 유저면 소속구분(Step 4)으로 직행
      if (currentStep === 6 && formData['orgType'] !== '총무처/교무처') {
        prevStep = 4;
      }

      if(prevStep > 0) {
        showStep(prevStep);
      }
    }

    // 텍스트 인풋 체크 (버튼 활성화)
    function checkInput(stepId, inputId) {
      const val = document.getElementById(inputId).value.trim();
      const btn = document.getElementById('btn-' + stepId);
      
      if(inputId === 'userPhone') {
        btn.disabled = val.length < 10;
      } else {
        btn.disabled = val.length === 0;
      }

      // 엔터키 치면 바로 다음으로
      const inputEl = document.getElementById(inputId);
      inputEl.onkeydown = function(e) {
        if(e.key === 'Enter' && !btn.disabled) {
          e.preventDefault();
          goNext();
        }
      };
    }

    // 체크박스 체크 (다중선택)
    function checkMulti(stepId, name) {
      const checked = document.querySelectorAll(`input[name="${name}"]:checked`).length > 0;
      document.getElementById('btn-' + stepId).disabled = !checked;
    }

    // 칩 버튼 클릭 (단일 선택 + 자동 넘어감)
    function selectChip(btn, key, value) {
      formData[key] = value;
      // UI 업데이트
      const chips = document.querySelectorAll(`#step${currentStep} .chip-btn`);
      chips.forEach(c => c.classList.remove('selected'));
      btn.classList.add('selected');
      
      // 0.3초 후 자동 넘어감 (훅훅 넘어가는 느낌)
      setTimeout(() => {
        goNext();
      }, 300);
    }

    // 마지막 예산 선택 (제출 활성화)
    function selectFinal(btn, key, value) {
      formData[key] = value;
      const chips = document.querySelectorAll(`#step8 .chip-btn`);
      chips.forEach(c => {
        c.classList.remove('selected');
        c.querySelector('.check-icon').style.display = 'none';
      });
      btn.classList.add('selected');
      btn.querySelector('.check-icon').style.display = 'block';

      document.getElementById('submitBtn').disabled = false;
    }

    function submitForm() {
      const btn = document.getElementById('submitBtn');
      btn.innerHTML = '<i data-lucide="loader-2" class="spin"></i> 처리중...';
      lucide.createIcons();
      
      // 데이터 수집
      formData.userName = document.getElementById('userName').value;
      formData.userPhone = document.getElementById('userPhone').value;
      formData.univName = document.getElementById('univName').value;
      formData.deptRole = document.getElementById('deptRole').value;
      
      const purposes = [];
      document.querySelectorAll('input[name="purpose"]:checked').forEach(el => purposes.push(el.value));
      formData.purposes = purposes;

      console.log("제출 데이터:", formData);

      // 페이크 로딩 후 완료 화면
      setTimeout(() => {
        showStep(9);
      }, 1000);
    }

    // 파일 첨부 핸들러
    function handleFileUpload(input) {
      const btn = document.getElementById('btn-step5'); // 바뀐 step5에 맞게 id 수정
      const display = document.getElementById('fileNameDisplay');
      
      if(input.files && input.files[0]) {
        display.innerText = input.files[0].name;
        display.style.color = 'var(--text-main)';
        btn.innerText = '확인';
        btn.classList.add('selected'); // 시각적 효과
      } else {
        display.innerText = '클릭하여 파일 첨부하기';
        display.style.color = 'var(--accent)';
        btn.innerText = '건너뛰기';
      }
    }

    // 모달 제어
    function openModal(e) {
      e.preventDefault();
      const modal = document.getElementById('privacyModal');
      modal.style.display = 'block';
      setTimeout(() => modal.classList.add('show'), 10);
    }

    function closeModal(e) {
      e.preventDefault();
      const modal = document.getElementById('privacyModal');
      modal.classList.remove('show');
      setTimeout(() => modal.style.display = 'none', 300);
    }

    // 수정하기 (Step 1으로 돌아가기)
    function editForm() {
      // 폼 제출 버튼 원복
      const btn = document.getElementById('submitBtn');
      btn.innerHTML = '신청 완료하기';
      showStep(1);
    }
  
