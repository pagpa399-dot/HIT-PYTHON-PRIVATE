# %% [markdown]
# # Buổi 01 — Git và Python nền tảng
# ## Notebook ôn tập và bài tập về nhà
# **Họ tên:** ... · **Nhóm:** ...
# 
# Đọc phần ôn tập, chạy ví dụ, hoàn thành TODO và tự viết bài. Dữ liệu có sẵn trong file; bài học độc lập. `None`/`pass` là chỗ chờ điền. Chạy từ đầu sau khi làm và ghi ít nhất một ca kiểm tra của bạn. Nộp vào `buoi_01` trên GitHub. Phần Git chạy trong terminal; không chạy server chặn kernel trong notebook.

# %% [markdown]
# ## Phần I · Git/GitHub

# %% [markdown]
# ## 1. Ôn nhanh kiến thức
# 
# | Khái niệm/lệnh | Ý nghĩa |
# |---|---|
# | Git / GitHub | Git quản lý phiên bản; GitHub lưu repo từ xa và hỗ trợ cộng tác |
# | `git init` / `git clone` | Khởi tạo thư mục chưa có Git / lấy bản sao repo đã có |
# | `git status` | Xem trạng thái file và nhánh |
# | `git add` | Chọn thay đổi cho commit tiếp theo |
# | `git commit -m "..."` | Tạo phiên bản cục bộ |
# | `git push` | Gửi commit lên remote |
# | `.gitignore` | Bỏ qua file chưa được theo dõi, như `.venv/`, `__pycache__/` |
# Save, commit và push là ba việc khác nhau. Clone rồi thì không cần init lại. Tên/email trong git config là tác giả commit, không thay cho đăng nhập.
# 

# %% [markdown]
# ## 2. Ví dụ để đọc và chạy
# 

# %% [markdown]
# Ví dụ Python duy nhất cần dùng hôm nay: chạy cell này hoặc lưu vào `hello.py`.
# 

# %%
print("Xin chao CLB Python!")


# %% [markdown]
# ## Bài A · Điền lệnh còn thiếu (cơ bản)
# Điền tên lệnh ngắn vào mỗi biến; mẫu: `check_state = "status"`. Chưa cần hiểu sâu cú pháp Python ở buổi này, chỉ thay `None` bằng chuỗi.
# 

# %%
check_state = "status"
select_changes = "add"
save_version = "commit"
send_to_github = "push"
copy_existing_repo = "clone"
start_empty_repo = "init"


# %% [markdown]
# **Tự kiểm tra:** ô dưới đã được chuẩn bị; hãy chạy sau khi hoàn thành phần TODO.
# 

# %%
answers = [check_state, select_changes, save_version, send_to_github, copy_existing_repo, start_empty_repo]
if any(value is None for value in answers):
    print("Chua hoan thanh: dien ca 6 lenh.")
else:
    assert answers == ["status", "add", "commit", "push", "clone", "init"]
    print("Dat: ban phan biet duoc cac lenh co ban.")


# %% [markdown]
# ## Bài B · Tự nộp bài đầu tiên (cơ bản)
# 
# 1. Tạo repo GitHub có README rồi clone về máy.
# 2. Tạo `hello.py` in ba dòng: tên, ngành/lớp và mục tiêu học Python; tạo `.gitignore`.
# 3. Dùng status → add → commit → push; mở GitHub kiểm tra file.
# 4. Đổi một dòng, commit/push lần hai. Dán URL repo và hai mã commit vào các biến bên dưới.
# **Minh chứng đạt:** leader xem được repo, chạy được hello.py, lịch sử có hai commit khác nhau. Ô dưới chỉ kiểm tra bạn đã điền minh chứng, không xác minh GitHub thay leader.
# 

# %%
repo_url = "https://github.com/pagpa399-dot/HIT-PYTHON-PRIVATE"
first_commit = "https://github.com/pagpa399-dot/HIT-PYTHON-PRIVATE/commit/386ffc78bb48490da35e9320f7e4d69a806703f2"
second_commit = "https://github.com/pagpa399-dot/HIT-PYTHON-PRIVATE/blob/main/hello.py"


# %% [markdown]
# **Tự kiểm tra:** ô dưới đã được chuẩn bị; hãy chạy sau khi hoàn thành phần TODO.
# 

# %%
if any(x is None for x in [repo_url, first_commit, second_commit]):
    print("Chua hoan thanh: dien URL va hai ma commit sau khi thao tac that.")
else:
    assert str(repo_url).startswith("https://github.com/")
    assert len(str(first_commit)) >= 7 and len(str(second_commit)) >= 7
    assert first_commit != second_commit
    print("Da dien minh chung; leader se kiem tra repo va lich su.")


# %% [markdown]
# ## Phần II · Python nền tảng

# %% [markdown]
# ## 1. Ôn nhanh kiến thức
# 
# - `int`: số nguyên; `float`: số thực; `str`: chuỗi; `bool`: True/False.
# - `=` gán giá trị; tên biến dùng snake_case, không bắt đầu bằng số.
# - `input()` trả về chuỗi: cần `int(...)`/`float(...)` khi tính toán số.
# - `+ - * / // % **`; dùng ngoặc để thể hiện đúng công thức.
# - `print()` hiển thị; f-string đưa biến vào chuỗi. `:.2f` định dạng hiển thị, không sửa giá trị gốc.
# - `"2" + "3"` là `"23"`; `2 + 3` là `5`. `/` khác `//`.
# - Traceback: đọc tên lỗi ở dòng cuối rồi tìm dòng code của mình. Buổi này giả định dữ liệu số đúng định dạng; xử lý exception học ở buổi 7.
# 

# %% [markdown]
# ## 2. Ví dụ để đọc và chạy
# 

# %%
name = "Lan"
minutes = 125
print(f"Xin chao {name}")
print(minutes // 60, "gio", minutes % 60, "phut")
print(f"7 / 2 = {7 / 2:.2f}")


# %% [markdown]
# ## Bài A · Điền phép tính (cơ bản)
# Cho điểm 8, 7, 9. Điền trung bình và chuỗi báo cáo `Diem trung binh: 8.00`.
# 

# %%
math_score = 8
english_score = 7
python_score = 9
average_score = (math_score + english_score + python_score ) / 3  # TODO: cong ba diem roi chia 3
report = f"Diem trung binh: {average_score:.2f}"  # TODO: f-string, hai chu so thap phan


# %% [markdown]
# **Tự kiểm tra:** ô dưới đã được chuẩn bị; hãy chạy sau khi hoàn thành phần TODO.
# 

# %%
if average_score is None or report is None:
    print("Chua hoan thanh Bai A.")
else:
    assert average_score == 8
    assert report == "Diem trung binh: 8.00"
    print("Dat Bai A.")


# %% [markdown]
# ## Bài B · Chuyển kiểu và đổi thời gian (cơ bản)
# Dữ liệu nhập được mô phỏng bằng chuỗi `"185"`. Chuyển sang int, tính số giờ/phút còn lại. Không dùng vòng lặp/hàm vì chưa học.
# 

# %%
minutes_text = "185"
total_minutes = int(minutes_text)
hours = total_minutes // 60
remaining_minutes = total_minutes % 60


# %% [markdown]
# **Tự kiểm tra:** ô dưới đã được chuẩn bị; hãy chạy sau khi hoàn thành phần TODO.
# 

# %%
if any(x is None for x in [total_minutes, hours, remaining_minutes]):
    print("Chua hoan thanh Bai B.")
else:
    assert isinstance(total_minutes, int)
    assert (hours, remaining_minutes) == (3, 5)
    print("Dat Bai B: 3 gio 5 phut.")


# %% [markdown]
# ## Tự viết thêm
# Viết chương trình nhập tên và hai số, in tổng/hiệu/tích bằng f-string. Chạy file `.py` trong terminal rồi commit/push. Chưa cần vòng lặp hoặc hàm.

# %%
name = input("Nhap ten: ")
a = float(input("Nhap so: "))
b = float(input("Nhap so: "))
tong = a + b
hieu = a - b
tich = a * b        
print(f"{name}")
print(f"Tong: {tong}")
print(f"Hieu: {hieu}")
print(f"Tich: {tich}")# TODO: viết chương trình riêng và ghi minh chứng Git

# %% [markdown]
# ## Tự đánh giá và nộp bài
# - [ ] Đã hoàn thành bài cơ bản và chạy ô kiểm tra.
# - [ ] Đã thêm một ca thử mới, giải thích được kết quả.
# - [ ] Đã khởi động lại kernel và chạy các cell từ đầu.
# - [ ] Đã lưu notebook, commit/push và kiểm tra trên GitHub.
# 
# **Nhận xét của em:** bước khó nhất, lỗi đã gặp và cách sửa (3–5 câu).


