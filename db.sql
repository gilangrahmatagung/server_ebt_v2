CREATE TABLE tb_data (
	data_id INT auto_increment NOT NULL,
	raspi_id INT NULL,
	source varchar(50) NOT NULL,
	sensor varchar(50) NULL,
	current FLOAT NULL,
	voltage FLOAT NULL,
	power FLOAT NULL,
	api_created_at DATETIME NULL,
	db_created_at DATETIME DEFAULT current_timestamp NOT NULL,
	CONSTRAINT tb_data_pk PRIMARY KEY (data_id)
)
ENGINE=InnoDB
DEFAULT CHARSET=utf8mb4
COLLATE=utf8mb4_general_ci;