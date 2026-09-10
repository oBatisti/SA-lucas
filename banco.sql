CREATE DATABASE IF NOT EXISTS barbearia;
USE barbearia;

CREATE TABLE IF NOT EXISTS agendamentos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    cliente VARCHAR(100) NOT NULL,
    telefone VARCHAR(20),
    servico VARCHAR(100),
    preco DECIMAL(10, 2),
    barbeiro VARCHAR(50),
    data DATE NOT NULL,
    horario TIME NOT NULL,
    status VARCHAR(20) NOT NULL DEFAULT 'Agendado'
);

INSERT INTO agendamentos (cliente, telefone, servico, preco, barbeiro, data, horario, status) VALUES
('Ana Souza', '11987654321', 'Corte feminino', 65.00, 'Lucas', '2026-09-12', '09:00:00', 'Agendado'),
('Bruno Lima', '11976543210', 'Corte masculino', 45.00, 'Rafael', '2026-09-12', '10:00:00', 'Agendado'),
('Carla Mendes', '11965432109', 'Barba', 35.00, 'Lucas', '2026-09-12', '11:30:00', 'Concluído'),
('Diego Alves', '11954321098', 'Corte e barba', 70.00, 'Rafael', '2026-09-13', '09:30:00', 'Cancelado'),
('Elisa Rocha', '11943210987', 'Hidratação', 55.00, 'Marcos', '2026-09-13', '14:00:00', 'Agendado'),
('Felipe Costa', '11932109876', 'Corte masculino', 45.00, 'Lucas', '2026-09-14', '08:30:00', 'Concluído'),
('Gabriela Nunes', '11921098765', 'Corte feminino', 65.00, 'Marcos', '2026-09-14', '10:30:00', 'Agendado'),
('Henrique Silva', '11910987654', 'Barba', 35.00, 'Rafael', '2026-09-14', '15:00:00', 'Cancelado');
