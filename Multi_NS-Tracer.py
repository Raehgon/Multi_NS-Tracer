import subprocess
import threading
import concurrent.futures
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import messagebox

# Funções de execução de tracert e nslookup
def run_tracert(target_ip):
    try:
        result = subprocess.run(['tracert', target_ip], capture_output=True, text=True, shell=True)
        return target_ip, result.stdout
    except Exception as e:
        return target_ip, str(e)

def run_nslookup(target_domain, dns_server):
    try:
        result = subprocess.run(['nslookup', target_domain, dns_server], capture_output=True, text=True, shell=True)
        return target_domain, result.stdout
    except Exception as e:
        return target_domain, str(e)

# Função para criar relatório em arquivo .txt
def create_txt_report(report_data):
    with open("report.txt", "w", encoding='utf-8') as f:
        for target, result in report_data.items():
            f.write(f"Target: {target}\n{result}\n{'='*50}\n")
    messagebox.showinfo("Relatório Criado", "Relatório TXT criado com sucesso!")

# Função para atualizar a barra de progresso
def update_progress_bar(progress, text_label):
    text_label.config(text=f"{progress.get():.0f}%")
    progress_bar.update()

# Função para executar testes
def execute_tests():
    def run_tests():
        target_ips = ip_entry.get().split(',')
        target_domains = domain_entry.get().split(',')
        dns_server = dns_entry.get()

        report_data = {}
        total_tasks = len(target_ips) + len(target_domains)
        completed_tasks = 0

        with concurrent.futures.ThreadPoolExecutor() as executor:
            future_to_ip = {executor.submit(run_tracert, ip.strip()): ip.strip() for ip in target_ips}
            future_to_domain = {executor.submit(run_nslookup, domain.strip(), dns_server): domain.strip() for domain in target_domains}

            for future in concurrent.futures.as_completed(future_to_ip):
                ip, tracert_result = future.result()
                report_data[ip] = tracert_result
                completed_tasks += 1
                progress.set(completed_tasks / total_tasks * 100)
                update_progress_bar(progress, progress_label)

            for future in concurrent.futures.as_completed(future_to_domain):
                domain, nslookup_result = future.result()
                report_data[domain] = nslookup_result
                completed_tasks += 1
                progress.set(completed_tasks / total_tasks * 100)
                update_progress_bar(progress, progress_label)

        result_text.delete('1.0', 'end')

        for target, result in report_data.items():
            result_text.insert('end', f"Target: {target}\n{result}\n{'='*50}\n")

        generate_button.config(state='normal')
        generate_button.report_data = report_data

    progress.set(0)
    progress_label.config(text="0%")
    generate_button.config(state='disabled')
    threading.Thread(target=run_tests).start()

# Configurações da interface ttkbootstrap
root = ttk.Window(themename="cyborg")
root.title("Teste Tracert e Nslookup Múltiplo")
root.geometry("800x600")

# Frame principal para organização dos widgets
main_frame = ttk.Frame(root)
main_frame.pack(padx=20, pady=20, fill='both', expand=True)

# Frame para os inputs do usuário
input_frame = ttk.Frame(main_frame)
input_frame.pack(side='left', fill='both', expand=True, padx=(0, 20))

ip_label = ttk.Label(text="INFO: Separe com virgula caso seja mais de um IP, DOMINIO E DNS")
ip_label.pack(padx=10, pady=(20, 5))

ip_label = ttk.Label(input_frame, text="Endereços IP:")
ip_label.pack(padx=10, pady=(20, 5))

ip_entry = ttk.Entry(input_frame, font=("Arial", 10))
ip_entry.pack(padx=10, pady=5)

domain_label = ttk.Label(input_frame, text="Domínios:")
domain_label.pack(padx=10, pady=(20, 5))

domain_entry = ttk.Entry(input_frame, font=("Arial", 10))
domain_entry.pack(padx=10, pady=5)

dns_label = ttk.Label(input_frame, text="Servidor DNS:")
dns_label.pack(padx=10, pady=(20, 5))

dns_entry = ttk.Entry(input_frame, font=("Arial", 10))
dns_entry.pack(padx=10, pady=5)

execute_button = ttk.Button(input_frame, text="Executar Testes", command=execute_tests, bootstyle=SUCCESS)
execute_button.pack(padx=10, pady=(20, 10))

# Variável de progresso e rótulo de progresso
progress = ttk.DoubleVar()
progress_label = ttk.Label(input_frame, text="0%", font=("Arial", 10))
progress_label.pack(padx=10, pady=(10, 5))

progress_bar = ttk.Progressbar(input_frame, variable=progress, bootstyle="SUCCESS-striped", length=200)
progress_bar.pack(padx=10, pady=(5, 20))

generate_button = ttk.Button(input_frame, text="Gerar Relatório", command=lambda: create_txt_report(generate_button.report_data), state='disabled', bootstyle=SUCCESS)
generate_button.pack(padx=10, pady=(0, 10))

# Textbox para os resultados
result_text = ttk.ScrolledText(main_frame, height=15, width=80, font=("Arial", 10))
result_text.pack(side='right', fill='both', expand=True)

root.mainloop()
